import pandas as pd
import os

# data 파일 경로
path = r"C:\유튜브\pandas\data"
fileName = "easySample_woHeader.csv" # Head가 없는 CSV
file = os.path.join(path, fileName)

df=pd.read_csv(file) # option 없이 DataFrame 생성
print(df.head(2)) # 첫번째 자료가 columns로 전환됨.

df=pd.read_csv(file,header=None) # 'head=' option None으로 설정
print(df.head(2)) # Range Index로 column이 지정됨

# 컬럼 지정 : header=None,names=[컬럼명,,,,,,,]
df=pd.read_csv(file,header=None,names=['ID','이름','생일','학과','영어','일본어','중국어'])
print(df.head(2))

# 컬럼 및 index지정 : header=None,names=[컬럼명,,,,,,,],index_col='컬럼명'
df=pd.read_csv(file,header=None,
               names=['ID','이름','생일','학과','영어','일본어','중국어'],
               index_col='ID')
print(df.head(2))