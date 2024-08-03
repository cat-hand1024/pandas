import pandas as pd

file = ".\data\easySample2.csv"

df=pd.read_csv(file)

df=df[['pname','dept','birth']]
df.index=pd.Index(list('ABCDEFGHIJ'))
# DataFrame의 basice indexer는 index를 기준으로 한다.

print(df[3:7])
print(df['D':'F'])

# boolean indexer : 컬럼(Series)의 값을 조건으로 필터링 DataFrame indexer
# 일종의 필터링 효과
print(df[df['dept']=='Education']) # dept가 Education인 자료 필터링
print(df[(df['dept']=='Education')|( df['dept']=='Sales')]) # dept가 Education 혹은 Sales 필터링
print(df[df['dept'].isin(['Education','Sales'])]) # isin메서드 사용 필터링
print(df[~(df['dept'].isin(['Education','Sales']))]) # Education,Sales 제외한 필터링

