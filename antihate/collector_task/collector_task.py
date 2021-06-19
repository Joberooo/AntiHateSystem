import threading
import time
import pandas as pd
from datetime import datetime


class CollectorTask:

    def __init__(self, hate_analyzer, path_to_raw_data, interval):
        self.__interval = interval
        self.__path_to_raw_data = path_to_raw_data
        self.__hate_analyzer = hate_analyzer
        self.__run = False

    def start(self):
        def loop():
            while self.__run:
                time.sleep(self.__interval)
                threading.Thread(
                    target=self.__collect_data(),
                    name="CollectorTask.__collect_data",
                    daemon=True
                ).start()

        self.__run = True
        threading.Thread(
            target=loop,
            name="CollectorTask",
            daemon=True
        ).start()

    def stop(self):
        self.__run = False

    def __collect_data(self):
        stats = self.__hate_analyzer.get_stats()
        try:
            df_old = pd.read_csv(self.__path_to_raw_data)
        except FileNotFoundError:
            df_old = pd.DataFrame()
            df_old.index.name = "index"
        new_values_df = pd.DataFrame(data=stats)
        now = datetime.now()
        new_values_df['time'] = pd.Series([now for x in range(len(new_values_df.index))])
        df2 = pd.concat([df_old, new_values_df])

        df2.to_csv(self.__path_to_raw_data, index=False)
