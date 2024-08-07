import pandas as pd

file='.\data\easySample2.csv'

df=pd.read_csv(file,index_col='ID')

print(df.info()) # info() 메서드 활용
print(df.isna()) # isna() 메서드

# 컬럼 지정 nan 확인
# english 컬럼 nan 확인

print(df['english'].isna()) # 각 value의 nan 유무 boolean으로 표시
print(df['english'].isna().any()) # 하나라로  True 이면 True
print(df['english'].isna().sum()) # True 갯수 함 -> nan 합

df1=df[['english','japanese','chinese']]

# 각 index별 자료 확인
# nan가 없는 경우
print(df1[~df1.isna().any(axis='columns')])
print(df1[df1.notna().all(axis='columns')])
# 모두가 nan인 경우
print(df1[df1.isna().all(axis='columns')])
print(df1[~df1.notna().any(axis='columns')])

