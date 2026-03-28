import pandas as pd

df = pd.read_csv('customers-100.csv')
df2 = pd.read_json('pretty-print.json')#print(df2)
#SELECTIon by column
print(df["variety"])

#print(df)#for printing all of it ->print(df.to_string())