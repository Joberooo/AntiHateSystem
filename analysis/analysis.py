import asyncio
import threading
from datetime import datetime, timedelta
from time import sleep

from settings.settings import get_parm
import pandas as pd


class Analysis:
    def __init__(self):
        self.__last_datatime = None
        self.__interval = get_parm('analysis_interval')
        self.__path_to_data = get_parm('csv_file_name')
        self.__limit_hate_ratio = get_parm('limit_hate_ratio')
        self.__limit_hate_sum = get_parm('limit_hate_value')
        self.__run = False

    def start(self):
        def loop():
            while self.__run:
                sleep(self.__interval)
                t = threading.Thread(target=self.__get_stats_for_last_period(), name="__get_stats_for_last_period")
                t.daemon = True
                t.start()

        self.__run = True
        t = threading.Thread(target=loop, name="loop")
        t.daemon = True
        t.start()

    def stop(self):
        self.__run = False

    def __get_stats_for_last_period(self):
        df = pd.read_csv(self.__path_to_data)
        df['Time'] = pd.to_datetime(df['Time'])
        newest = df['Time'].max()
        last = (newest - timedelta(seconds=self.__interval) + timedelta(
            milliseconds=10)) if self.__last_datatime is None else self.__last_datatime
        mask = (df['Time'] > last) & (df['Time'] <= newest)
        sub_df = df.loc[mask]
        self.__analise_sub_data(sub_df)

    def __analise_sub_data(self, df: pd.DataFrame):
        hate_sum = 0

        for row in df.itertuples():
            hate_ratio = row.offensive_language + row.hate_speech
            if hate_ratio >= self.__limit_hate_ratio:
                hate_sum = hate_sum + 1
        if hate_sum > self.__limit_hate_sum:
            return True
        return False
