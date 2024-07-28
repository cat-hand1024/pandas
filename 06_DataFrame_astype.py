import pandas as pd
import os

# data 파일 경로
path = r"C:\유튜브\pandas\data"
fileName = "astype_sample.csv" # Head가 없는 CSV
file = os.path.join(path, fileName)

df=pd.read_csv(file)
print(df.dtypes)

# column 단독변경
df['english']=df['english'].astype('int32')
print(df.dtypes)

# 특정 데이터 타입만 변경
cols=df.columns[df.dtypes=='int64']
df[cols]=df[cols].astype('int32')
print(df.dtypes)

# 컬럼별 데이터 타입 지정 - 딕셔너리 방식
changeType={'ID':'float','english':'float'}
df=df.astype(changeType)
print(df.dtypes)
