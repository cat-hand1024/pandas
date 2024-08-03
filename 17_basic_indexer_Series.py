import pandas as pd

file = ".\data\easySample2.csv"

df=pd.read_csv(file)

df=df[['pname','dept','birth','overtime']]
df.index=pd.Index(list('ABCDEFGHIJ'))
print(df)

# Series의 basic indexer

sr=df['pname']

# 1개의 index indexing
# 첫번째 요소
print(sr.iloc[0]) # index번호 indexer
print(sr['A']) # index value indexer

# 마지막 요소
print(sr.iloc[-1]) #마지막 요소

# 다중 index indexing
# index list
print(sr[['A','C','F']])
# slicing
print(sr.iloc[3:])

# boolean indexer

# 이름 첫자가 J인 사람 추출
print(sr[sr.str.startswith('J')])

# 이름 마지막이 'k'인 사람
print(sr[sr.str.endswith('k')])

# 이름에 'am'이 포함된 사람
print(sr[sr.str.contains('am')])
