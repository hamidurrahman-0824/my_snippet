import pandas as pd
df = pd.read_csv("/home/dwgls/my_snippet/synthetic_dataset.csv")
#df = df.dropna(subset=["Price"])
#df = df.dropna(subset=["Price"])
"""
h = df.head()
price = round(df["Price"].mean(),2)
m = df["Price"].max()
mn = df["Price"].min()
n = round(df.groupby("Category")["Price"].mean(),2)
#n = df.groupby("Category")["Price"].mean().round(2).to_string()
st = f""""""Avg. Price {price}
Max Price {m}
Min Price {mn}
Avg Price per Category {n}"""
"""
#combo
summary = df["Price"].agg(["mean", "max", "min"]).round(2)
print(summary)


"""
df = df.dropna(subset=["Stock"])
stock = df.groupby("Stock").size().to_string()
hrating = df.groupby("Category")["Rating"].sum()
print(hrating)
