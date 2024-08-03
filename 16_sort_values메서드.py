import pandas as pd

# df.sort_values(by,axis=,ascending=,inplace=)

file = ".\data\easySample2.csv"

df=pd.read_csv(file,index_col='ID')

df1=df.sort_values(by='pname')
print(df1)

df2=df.sort_values(by=['pname','birth'],ascending=[False,True]) # pname 오름차순,.birth 내림차순
print(df2)