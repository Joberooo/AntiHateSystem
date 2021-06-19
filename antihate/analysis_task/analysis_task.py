import json
import threading
from datetime import timedelta
from time import sleep

import pandas as pd


class AnalysisTask:
    def __init__(self, interval, path_to_raw_data, path_to_stats_file,hate_ratio_limit, hate_sum_limit, email_sender):
        self.__last_to_datetime = None
        self.__interval = interval
        self.__path_to_raw_data = path_to_raw_data
        self.__hate_ratio_limit = hate_ratio_limit
        self.__hate_sum_limit = hate_sum_limit
        self.__path_to_stats_file = path_to_stats_file
        self.__email_sender = email_sender
        self.__run = False

    def start(self):
        def loop():
            while self.__run:
                sleep(self.__interval)
                threading.Thread(
                    target=self.__check_stats(),
                    name="AnalysisTask.__check_stats()",
                    daemon=True
                ).start()

        self.__run = True
        threading.Thread(
            target=loop,
            name="AnalysisTask",
            daemon=True
        ).start()


    def stop(self):
        self.__run = False

    def __check_stats(self):
        try:
            df = pd.read_csv(self.__path_to_raw_data)
        except FileNotFoundError:
            return
        df['time'] = pd.to_datetime(df['time'])
        to_date = df['time'].max()
        from_date = (to_date - timedelta(seconds=self.__interval) + timedelta(
            milliseconds=10)) if self.__last_to_datetime is None else self.__last_to_datetime
        self.__last_to_datetime = to_date
        mask = (df['time'] > from_date) & (df['time'] <= to_date)
        sub_df = df.loc[mask]
        if self.__check_last_period(sub_df, from_date, to_date):
            self.__email_sender.send_notification()

    def __check_last_period(self, df: pd.DataFrame, from_date, to_date):
        hate_sum = 0

        for row in df.itertuples():
            hate_ratio = row.offensive_language + row.hate_speech
            if hate_ratio >= self.__hate_ratio_limit:
                hate_sum = hate_sum + 1
                if hate_sum >= self.__hate_sum_limit:
                    self.__save_stats(df, from_date, to_date)
                    return True
        return False

    def __save_stats(self, df: pd.DataFrame, from_date, to_date):
        rows_with_hate, offensive_language_counter, hate_speech_counter = self.__get_stats(df)
        try:
            with open(self.__path_to_stats_file, "r") as read_file:
                json_data = json.load(read_file)
        except FileNotFoundError:
            json_data = {
                "stats": []
            }
        json_data["stats"].append(
            {
                "from_date": from_date.isoformat(),
                "to_date": to_date.isoformat(),
                "offensive_language": offensive_language_counter,
                "hate_speech": hate_speech_counter,
                "data": rows_with_hate
            }
        )
        with open(self.__path_to_stats_file, 'w') as f:
            json.dump(json_data, f, indent=4)
            return None

    def __get_stats(self,df):
        rows_with_hate = []
        offensive_language_counter = 0
        hate_speech_counter = 0

        for row in df.itertuples():
            hate_ratio = row.offensive_language + row.hate_speech
            if hate_ratio >= self.__hate_ratio_limit:
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
        print("rows_with_hate")
        print(rows_with_hate)
        return rows_with_hate, offensive_language_counter, hate_speech_counter
