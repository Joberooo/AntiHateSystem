import asyncio

from hateanalyzer.hate_analyzer import HateAnalyzer
from settings.settings import get_parm
import pandas as pd
from datetime import datetime


class Collector:

    def __init__(self):
        self.__interval = get_parm("collect_interval")
        self.__data_path = get_parm("csv_file_name")
        self.__hateanalyzer = HateAnalyzer()
        self.__run = False

    async def start(self):
        self.__run = True
        while self.__run:
            await asyncio.sleep(self.__interval)
            self.__collect_data()

    def stop(self):
        self.__run = False

    async def __collect_data(self):
        stats = self.__hateanalyzer.get_stats()
        try:
            df_old = pd.read_csv(self.__data_path)
        except FileNotFoundError:
            df_old = pd.DataFrame()
            df_old.index.name = "Index"
        new_values_df = pd.DataFrame(data=stats)
        now = datetime.now()
        new_values_df['Time'] = pd.Series([now for x in range(len(new_values_df.index))])
        df2 = pd.concat([df_old, new_values_df])

        df2.to_csv(self.__data_path, index=False)
