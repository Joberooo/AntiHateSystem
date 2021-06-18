from settings.settings import get_parm
import pandas as pd
from datetime import datetime



class Collector:

    def __init__(self):
        self.interval = get_parm("collect_interval")
        self.data_path = get_parm("csv_file_name")
        self.hateanalyzer = HateAnalyzer()

    def collect_data(self):
        stats = self.hateanalyzer.get_stats()
        try:
            df_old = pd.read_csv(self.data_path)
        except FileNotFoundError:
            df_old = pd.DataFrame()
            df_old.index.name = "Index"
        newValuesDf = pd.DataFrame(data=stats)
        newValuesDf['Time'] = pd.Series([datetime.now() for x in range(len(newValuesDf.index))])
        df2 = pd.concat([df_old, newValuesDf])

        df2.to_csv(self.data_path,index=False)
