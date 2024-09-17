import pandas as pd

df = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

country_summary = df.groupby('country').agg(count = ('points', 'size'), points = ('points', 'mean')).reset_index()

country_summary['points'] = country_summary['points'].round(1)

country_summary.to_csv('data/reviews-per-country.csv', index = False)

print(country_summary.head())