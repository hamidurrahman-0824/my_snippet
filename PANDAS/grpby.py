import pandas as pd
df = pd.read_csv("C:\\Users\\user\\my_snippet\\synthetic_dataset.csv",encoding="utf-8")
obj = df.groupby("Category")
sz = obj.size()
cmean = obj["Discount"].mean()
crate = df.groupby("Category")["Rating"].mean()
exact_1_cat = crate = df.groupby("Category")["Rating"].mean().loc["A"]#-> 

cprice = df.groupby("Category")["Price"].sum()
#multiple aggregation
mul = obj.agg({"Price":['mean','max','min']})

#mul grouby
ob = df.groupby(["Category","Stock"])
#print(ob.count())
#BASIC SYNTAX df.groupby("colums")["Value colums"].aggregation()
#count items per group
g = df.groupby("Category").size()
print(g)
#alt
g = df["Category"].value_counts()
print(g)
#multi-aggr
g = df.groupby("Category")
"""print(g.agg({"cols":['max','mean','min']}))
         g.agg(['mean','max',min','count'])"""
#mulcol
df.groupby("Category").agg(
    avg_price=("Price","mean"),
    max_price=("Price","max"),
    product_count=("Price","count")
)
g = df.groupby(["Category","Stock"])["Price"].mean()
#reset index 
df.groupby("Category")["Price"].mean().reset_index()
#show categories rating above 4
df.groupby("Category")["Rating"].mean().loc[lambda x: x > 4]
#top revenue categories
df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
#most popular drinks
df.groupby("coffee_name").size().sort_values(ascending=False)
df.groupby("Category").agg(
    avg_rating=("Rating","mean"),
    avg_price=("Price","mean"),
    total_products = ("Price","count")
)
#top rated product per category
df.sort_values("Rating",ascending=False).groupby("Category").head(1)
#pivot style summary
df.groupby(["Category","Stock"])["Price"].mean().unstack()