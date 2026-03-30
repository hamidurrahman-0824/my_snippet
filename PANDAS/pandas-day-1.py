import pandas as pd
df = pd.read_csv("data.csv")
#select columns
# print(df["Name"])#df.loc[:,"Name"]
# print(df["Age"])
# print(df["Score"])
print(df.loc[0])
#select rows
"""use iloc unless index_col was not set, else df.loc["index_row element"]"""
print(df.loc[[0,1,2]])
