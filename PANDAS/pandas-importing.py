import pandas as pd

df = pd.read_csv('customers-100.csv')
df2 = pd.read_json('pretty-print.json')#print(df2)
#SELECTIon by column
result = df["First Name"]
result = df["Phone 2"]
result = df["Website"]
result = df[["First Name","Phone 2","Website"]]#multiple column selection
#SELECTIONBY ROW/s

result = df.loc[[0,1,2]]
df = pd.read_csv("customers-100.csv",index_col="Last Name")#->df.loc[any last name]#index_col = any column head i want
result = df.loc["Baxter",["Email","Website"]]#second arg as list
result = df.loc["Baxter":"Berry",["Email","Website"]]#slice can be used
result = df.iloc[0:11]#first 10 row
result = df.iloc[0:10,2]#first 10 row
result = df.iloc[0:11:2,0:3]#full slicing is used here
print(result)
#print(df)#for printing all of it ->print(df.to_string())
customer = input('Enter a last name :')#-> last name because we set index manually as index_col = last name,now index is no more 0,1...
try:
    print(df.loc[customer])
except KeyError:
    print(f"{customer} not found.")