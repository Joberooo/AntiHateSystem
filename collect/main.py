import asyncio

import pandas as pd

from collect.collector import Collector, HateAnalyzer

if __name__ == "__main__":
    collector = Collector()
    collector.start()
    await asyncio.sleep(1000)
    collector.stop()


