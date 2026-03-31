#loc,iloc,colum,single/multiple row selection

import pandas as pd
df = pd.read_csv("customers-100a.csv")
#single column:
single_col = df["Ages"]
multi_col = df[["Index","First Name","Email"]]
multi_col_slice = df.loc[:, "Index":"First Name"]#pashapashi sob, not slicing
mul_row_col = df.iloc[0::10,0::6]
even_col = df.iloc[0:2,0:2]
singe_element = df.loc[2,"Ages"]
#row selection
single_row = df[0:1]
single_row = df.loc[1]
mul_row = df[0:5]
mul_row_col = df.iloc[1:5,1:5]
#
arr = df[["Ages"]]
# print(arr)
# print(df["Ages"]>40)
print(df[df["Ages"].between(25,40) & df["Email"].str.contains("gmail|yahoo", case=False)])
df = pd.read_csv("customers-100a.csv",index_col="First Name")
#multi_row = df.loc[]
#filtering
df[
    df["Ages"].between(25,40)&
    df["Email"].str.contains("gmail|yahoo")
]
df[
    (df["Ages">=25]) & (df["Ages"]<=40) &
    (
        df["Email"].str.contains("gmail")|
        df["Email"].str.contains("yahoo")
    )
]
