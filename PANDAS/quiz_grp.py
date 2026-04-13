import pandas as pd
df = pd.read_csv('synthetic_dataset.csv')
print(df.head(1))
"""
g_c = df.groupby("Category")
print(g_c["Rating"].mean())
print(g_c["Price"].sum())
g_s = df.groupby("Stock")
print(g_s.sum())
g_c_s = df.groupby(["Category","Stock"])
avg_rat = g_c_s["Rating"].mean()

print(g_c_s.count())
print(g_c_s.size())
print(df.groupby("Stock").size())#instock = 1513,out 1497
print(avg_rat)
"""
#category with highest avg
#print(df.groupby("Category")["Price"].mean().sort_values(ascending=False).head(1))
#second quiz'
import pandas as pd
df = pd.read_csv('synthetic_dataset.csv')
g = df.groupby("Stock")
#1
avg_price = g["Price"].mean()
#2
g = df.groupby("Category")
discount = g["Discount"].sum()
#5
highest_avg_rat = g["Rating"].mean().sort_values(ascending=False).head(1)
df.groupby("Category")["Rating"].mean().idxmax()
print(highest_avg_rat)
#3
num = g.size()#len
num = g.count()#non nan value
#4
g = df.groupby(["Category","Stock"])
avg_rat = g["Rating"].mean()
print(avg_rat)