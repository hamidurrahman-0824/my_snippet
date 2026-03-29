import pandas as pd
#dataframe, series
#load some data
df = pd.read_csv("sales_data.csv")

print(df.iloc[2])
exit()
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.info())
print(df.columns)

print(df.index)
