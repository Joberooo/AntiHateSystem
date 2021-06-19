import asyncio
import json
import threading
from datetime import datetime, timedelta
from time import sleep

from email_sender.email_sender import EmailSender
from settings.settings import get_parm
import pandas as pd


class Analysis:
    def __init__(self):
        self.__last_datatime = None
        self.__interval = get_parm('analysis_interval')
        self.__path_to_data = get_parm('csv_file_name')
        self.__limit_hate_ratio = get_parm('limit_hate_ratio')
        self.__limit_hate_sum = get_parm('limit_hate_sum')
        self.__email_sender = EmailSender()
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
        if self.__analise_sub_data(sub_df, last, newest):
            self.__email_sender.try_send("Temat", "nuu nu nu nu")

    def __analise_sub_data(self, df: pd.DataFrame, from_date, to_date):
        hate_sum = 0

        for row in df.itertuples():
            hate_ratio = row.offensive_language + row.hate_speech
            if hate_ratio >= self.__limit_hate_ratio:
                hate_sum = hate_sum + 1
                if hate_sum >= self.__limit_hate_sum:
                    self.__save_stats(df, from_date, to_date)
                    return True
        return False

    def __save_stats(self, df: pd.DataFrame, from_date, to_date):
        rows_with_hate = []
        offensive_language_counter = 0
        hate_speech_counter = 0

        for row in df.itertuples():
            hate_ratio = row.offensive_language + row.hate_speech
            if hate_ratio >= self.__limit_hate_ratio:
                if row.offensive_language > row.hate_speech:
                    offensive_language_counter = offensive_language_counter + 1
                else:
                    hate_speech_counter = hate_speech_counter + 1
                rows_with_hate.append({
                    "offensive_language": row.offensive_language,
                    "hate_speech": row.hate_speech,
                    "neither": row.neither,
                    "text": row.text
                })

        try:
            with open("../stats.json", "r") as read_file:
                json_data = json.load(read_file)
        except FileNotFoundError:
            json_data = {
                "stats": []
            }
        json_data["stats"].append(
            {
                "from_date": from_date.strftime('%m/%d/%Y %H:%M:%S'),
                "to_date": to_date.strftime('%m/%d/%Y %H:%M:%S'),
                "offensive_language": offensive_language_counter,
                "hate_speech": hate_speech_counter,
                "data": rows_with_hate
            }
        )
        print(json_data)
        with open('../stats.json', 'w') as f:
            json.dump(json_data, f, indent=4)
            return None
