import pandas as pd
df = pd.read_csv("C:\\Users\\user\\my_snippet\\synthetic_dataset.csv")
#isna()=isnan,if nan return True
isna = df.isna()

#notna()= notnan,if not Nan return True
notna = df.notna()
#

#check missing values
#print(df.isna().sum())#only df.isna() return true/false, sum add them and show total nan value
clean = df[df["Stock"] == "In Stock"]
#print(clean.dropna())

missing_discount = df["Discount"].isna()
print(missing_discount.sum())
missing_categories = df["Category"]
print(missing_categories,missing_categories.dropna())
print(missing_categories.fillna('F'))
print(df["Category"].fillna("FFF"))
print(df.head())
print(df[(df["Rating"].between(0,1.5))&(df["Stock"]== "In Stock")])