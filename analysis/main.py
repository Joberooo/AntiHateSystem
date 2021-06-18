from analysis.analysis import Analysis

if __name__ == '__main__':
    pathToCSVFile = 'woj.csv'
    analiza = Analysis()
    Analysis.doAnalisys(analiza, pathToCSVFile)