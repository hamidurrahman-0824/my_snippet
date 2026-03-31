import pandas as pd
import numpy as np
df = pd.read_csv("customers-100a.csv",index_col="Index")

#info = df.info()
#describe = df.describe()
shape = df.shape
mx = df["Ages"].max()#max min std etc
#read/write tabular data
"""pd.read_**()->pd.to_**()"""
head = df.head()
head_n = df.head(n=5)
dtypes = df.dtypes
interested_in_age = df["Ages"]
sample= df.sample(n=4)
#print(interested_in_age.head(3))interested_in_age.shape,size etc
intrstdin_age_sex = df[["Last Name","Phone 1"]]#.headtail etc
above_35 = df[df["Ages"]>=35]
above_35_and_has_dot_net = df[
    (df["Ages"]>=35) & 
    (df["Website"].str.contains(".net",case= False))
]

isin_country = df[df["Country"].isin(["Antigua and Barbuda"])]
specific_r_c = df.loc[df["Ages"]>=55,["First Name","Phone 1","Country"]]
itrstd_r1025 = df.iloc[10:26,3:6]
#setvalue = something like dictionary values
#df.iloc[0:3,3] = "Annonymous"

#aggregate function
#mean,median,describe,count
#groupby
group = df.groupby("City")
print(group["Ages"].mean())
mean_numeric_only = df.mean(numeric_only=True)
group_by_city = df.groupby(df["Ages"].between(24,30))

#groupby(city)-> creat a data frame,groupby(city)[colm].method
mean_age_country_wise = df.groupby("Country")["Ages"].mean()
mean_age_country_wise = df.groupby("Country").size()
mul_col_grp = df.groupby(["Country","City"]).size()#nothing works without method
#print(mul_col_grp)
df.groupby("Country").agg({
    "Ages":"mean",
    "Customer Id":"count"
})
by_agg = df.groupby("Country").agg({
    "Ages":"mean",
    "City":"count"
})
# print(by_agg)
see_grp = df.groupby("Country").groups
"""for country,group in df.groupby("Country"):
    print(country)
    print(group.head())
"""
#
# =# most used

df.groupby("Country").size()
df.groupby("Country")["Ages"].mean()
df.groupby("City").count()
df.groupby(["Country","City"]).size()


df.groupby("Country")["Ages"].agg("mean")
df.groupby("Country")["Ages"].agg(sum)
import numpy as np

df.groupby("Country")["Ages"].agg(np.mean)
df.groupby("Country")["Ages"].agg(["mean","max","min"])