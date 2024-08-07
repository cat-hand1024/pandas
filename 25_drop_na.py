import pandas as pd

file='.\data\easySample2.csv'

df=pd.read_csv(file,index_col='ID')

# dropna(axis=,how=,thresh=,subset=,inplace=)

df1=df[['english','japanese','chinese']]
print(df1)

df_allNa_drop=df1.dropna(axis='index',how='all') # index를 삭제한다.
print(df_allNa_drop)

df_anyNa_drop=df1.dropna(axis='index',how='any')
print(df_anyNa_drop)

df_NaCount2_drop=df1.dropna(axis='index',thresh=2) # nan이 2개 이상인 index 제거
print(df_NaCount2_drop)

df_columnChoice_drop=df1.dropna(axis='index',subset=['english']) # english컬럼의 nan인 index 삭제
print(df_columnChoice_drop)