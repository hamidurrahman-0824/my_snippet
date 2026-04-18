import pandas as pd
df = pd.read_csv("/home/dwgls/my_snippet/synthetic_dataset.csv")
grp = df.groupby("Category")
print(grp["Price"].sum())
print(df["Category"].value_counts().idxmax())
