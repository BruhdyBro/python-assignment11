import plotly.express as px
import plotly.data as pldata
import pandas as pd


df = pldata.wind(return_type='pandas')

print(df.head(20))

df['strength'] = df['strength'].str.replace(r"\D", ".", regex=True)

pd.to_numeric(df['strength'], errors='coerce')


fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title="Wind Direction, Strength vs. Frequency")
fig.write_html("wind.html", auto_open=True)