import pandas as pd
import os

# data 파일 경로
path = r"C:\유튜브\pandas\data"
fileName = "astype_sample.csv" # Head가 없는 CSV
file = os.path.join(path, fileName)

df=pd.read_csv(file,index_col='ID')
print(df.head(3))

# 컬럼 'birth'를 datatime으로 변경
df['birth']=pd.to_datetime(df['birth'])

# datatime 타입을 이용해서 년/월/일 추출하기
df['year']=df['birth'].dt.year
df['month']=df['birth'].dt.month
df['day']=df['birth'].dt.day

print(df[['birth','year','month','day']])

