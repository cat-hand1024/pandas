import pandas as pd


# pd.reset_index(level=,drop=False...)
file = ".\data\easySampleIndex.csv"
df=pd.read_csv(file,index_col='pname')

print(df)

df1=df.reset_index(level=0) # index이동
print(df1)

df2=df.reset_index(level=0,drop=True) # index 삭제
print(df2)