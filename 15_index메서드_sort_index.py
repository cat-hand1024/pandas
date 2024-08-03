import pandas as pd

# df.sort_index(axis=,level=,ascending=,inplace=,,,)

file = ".\data\easySample2.csv"

df=pd.read_csv(file,index_col='ID')

df_sortIndex_index=df.sort_index(axis='index',ascending=False) # 인덱스방향/내림차순

print(df_sortIndex_index)


df_sortIndex_columns=df.sort_index(axis='columns',ascending=False)
print(df_sortIndex_columns)