import pandas as pd

cities_df = pd.read_csv('resources/cities.csv')
cities_df.to_html('data.html', bold_rows=True, index=False)

data_table = df.to_html()
print(data_table)
