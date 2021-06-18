import asyncio
from settings.settings import get_parm
import pandas as pd


class Analisys:
    def __init__(self):
        self.analisysInterval = get_parm('analisys_interval')

    def doAnalisys(self, pathToCSVFile):
        # await asyncio.sleep(self.analisysInterval)
        csvFile = pd.read_csv(pathToCSVFile)
        print(csvFile)
