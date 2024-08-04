import pandas as pd

file='.\data\easySample2.csv'

df=pd.read_csv(file,index_col='ID')

print(df.loc[:,['pname','dept']])

print(df.loc['18030201':'18100000',['pname','dept']])