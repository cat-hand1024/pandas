import pandas as pd
import os

# data 파일 경로
path = r"C:\유튜브\pandas\data"
fileName = "easySample.csv" # Head가 없는 CSV
file = os.path.join(path, fileName)

df=pd.read_csv(file,index_col='ID')
print(df.head(3))

print(df.dtypes) # DataFrame의 데이터 타입확인 속성
print(df.info()) # DataFrame의 데이터 타입 및 null이 아닌 자료의 개수 확인 메서드