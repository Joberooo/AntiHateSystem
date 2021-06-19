from time import sleep

from analysis.analysis import Analysis
from collect.collector import Collector

def test_core():
    collector = Collector()
    collector.start()
    analysis = Analysis()
    analysis.start()
    sleep(140)
    collector.stop()
    analysis.stop()

if __name__ == "__main__":
    test_core()


