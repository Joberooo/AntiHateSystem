import pandas as pd

from collect.collector import Collector, HateAnalyzer

if __name__ == "__main__":
    stats = Collector().collect_data()

    print(stats)

