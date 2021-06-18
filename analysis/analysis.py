import asyncio
import threading
from datetime import datetime, timedelta, time

from settings.settings import get_parm
import pandas as pd


class Analysis:
    def __init__(self):
        self.__interval = get_parm('analysis_interval')
        self.path_to_data = get_parm('csv_file_name')
        self.__run = False

    def start(self):
        def loop():
            while self.__run:
                time.sleep(self.__interval)
                self.get_stats_for_last_period()
        self.__run = True
        t = threading.Thread(target=loop, name="loop")
        t.daemon = True
        t.start()

    def stop(self):
        self.__run = False

    def get_stats_for_last_period(self):
        df = pd.read_csv(self.path_to_data)
        now = datetime.now()
        mask = (df['Time'] > now - timedelta(seconds=self.__interval)) & (df['Time'] <= now)
        sub_df = df.loc[mask]
        print("DFAFDS")
        print(sub_df)
        print("DFAFDS")


