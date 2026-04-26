import pandas as pd
df = pd.read_csv("/home/dwgls/my_snippet/synthetic_dataset.csv")

g = df.groupby("Category")["Stock"].value_counts(ascending=True)


order = ["In Stock", "Out of Stock"]

g = (
    df.groupby("Category")["Stock"]
    .value_counts()
    .reindex(order, level=1)
)
table = df.groupby("Category")["Stock"].value_counts().unstack(fill_value=0)
g= df.groupby(["Stock","Category"])["Discount"].agg(['max','mean','min','sum'])

result = table.idxmax()
#oneliner
df.groupby("Category")["Stock"].value_counts().unstack(fill_value=0).idxmax()

g = df.groupby(["Category"])[["Discount","Price",'Rating']].mean().unstack().idxmax()
print(df[["Discount",'Rating']].corr())

exit()
#df = df.dropna(subset=["Price"])
df = df.dropna(subset=["Price"])
x = df.groupby("Category")["Price"].agg(['sum','max','mean','min'])
print(x)
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
prc = df["Stock"].value_counts(normalize=True)*100
tt = df.groupby("Stock").count()
maxminavg = df["Price"].agg(['mean','max','min'])
print(maxminavg)
