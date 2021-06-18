from datetime import time

from analysis.analysis import Analysis
from collect.collector import Collector


def test_core():
    collector = Collector()
    collector.start()
    analysis = Analysis()
    analysis.start()
    time.sleep(60)
    collector.stop()
    analysis.stop()