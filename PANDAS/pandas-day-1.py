import pandas as pd
data = [True,False,True,False,100,200,104,105,150,140]
series = pd.Series(data,index=['male','male','male','female','fucked','fucked','fucked','fucked','fucked','fucked'])
#locate:loc,series.loc["a"]
result = series.loc['male']
#index-locate:series.iloc[0]
result = series.iloc[4-1]
#filtering:series[series==True]
result = series[series>=150]
##usining dictionary
data ={
    "sepal.length": 5.1,
    "sepal.width": 3.5,
    "petal.length": 1.4,
    "petal.width": 0.2,
    "variety": 'Setosa'}
series = pd.Series(data)
#access-value:df.loc[]
result = series.loc['variety']
#update: seri.loc[] += ''#number for number string for string
series.loc['sepal.width'] += 0.1
#filtering: series[series>=,==,<= ]
#result = series[series>2]:remember comapring str and int
"""DataFrame"""
data = {
    "Name":['Majed','Fahmida','Sayem','Bushra','Rumana'],
    "Age":[23,27,30,33,38],
    "Honours_Passed":[True,True,True,True,True]
}
df = pd.DataFrame(data,index=['Earner 1','Earner 2','Earner 3','Earner 4','Earner 5'])
#loc: df.loc[label:earner1]
result = df.loc["Earner 1"]

#index-locate
#print(df.iloc[2])#only pass index of the most left colmn o dataframe
#add a new column
new_column = [True,True,True,True,True]
#df['Honours_Passed'] = new_column
#add a row
new_row = pd.DataFrame([{'Name':'Rokeya','Age':60,'Honours_Passed':False}],index=['Earner 6'])#for multiple row:pd.DataFrame([{},{},{}...]),index=[must have bracket]
new_rows = pd.DataFrame([{'Name':'Arob','Age':100,'Honours_Passed':False},
                          {'Name':'Alim','Age':50,'Honours_Passed':True}],index=['Earner 7','Earner 8'])
df = pd.concat([df,new_row,new_rows])#pass as many dataframe as needed inside list
print(df)
# print(df.loc[""])















exit()
data = [
  {
    "sepal.length": 5.1,
    "sepal.width": 3.5,
    "petal.length": 1.4,
    "petal.width": 0.2,
    "variety": "Setosa"
  },
  {
    "sepal.length": 4.9,
    "sepal.width": 3,
    "petal.length": 1.4,
    "petal.width": 0.2,
    "variety": "Setosa"
  },
  {
    "sepal.length": 4.7,
    "sepal.width": 3.2,
    "petal.length": 1.3,
    "petal.width": 0.2,
    "variety": "Setosa"
  }]
print(series)
print("")
print(result)
exit()
data = {
    "name": ["Alice","Bob","Charlie"],
    "age": [25,30,35]
}
dataframe = pd.DataFrame(data)
dataframe['sex'] = ['m','f','m']
new_row = ['Sandy',25,'f']
df = pd.DataFrame(new_row)
dataframe = pd.concat(df)
dataframe = dataframe + new_row#instead of row addition it will added to column


print(dataframe)
_1darray = [1,3,3,5]
series = pd.Series(_1darray)
# print(series)
csvfile = pd.read_csv('customers-100.csv')
# info = csvfile.info()
# describe = csvfile.describe()
# head = csvfile.head()
# tail = csvfile.tail()

exit()
class ToHighChodna(Exception):
    pass
raise ToHighChodna('You are to chodna to proceed.')