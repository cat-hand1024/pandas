import pandas as pd


file = ".\data\easySampleIndex.csv"

df=pd.read_csv(file,index_col='pname')
print(df.head(2))

# 특정 컬럼을 index로 전환 혹은 추가하는 기능
# df.set_index(keys,drop=True,append=False,inplace=False)

# age를 index로 대체하기
df_change=df.set_index(keys='age') #
print(df_change.head(2))

# age를 index에 추가하기
df_append=df.set_index(keys='age',append=True)
print(df_append.head(2))