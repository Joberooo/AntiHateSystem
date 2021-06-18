from hate_analyzer import HateAnalyzer

analyzer = HateAnalyzer()
stats = analyzer.get_stats()

for stat in stats:
    print(f'{stat}   =   {len(stat["text"])}')