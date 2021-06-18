import asyncio
import time

import pandas as pd

from collect.collector import Collector, HateAnalyzer

if __name__ == "__main__":
    collector = Collector()
    collector.start()
    time.sleep(60)
    collector.stop()


