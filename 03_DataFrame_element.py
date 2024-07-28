import pandas as pd
import os

# data 파일 경로
path = r"C:\유튜브\pandas\data"
fileName = "easySample_woHeader.csv" # Head가 없는 CSV
file = os.path.join(path, fileName)

df=pd.read_csv(file,header=None,names=['ID','이름','생일','학과','영어','일본어','중국어'],index_col='ID')

# index,columns,values
print(df.index)
print(df.columns)
print(df.values)

# index,columns의 values
print(df.index.values)
print(df.columns.values)

# index 이름
print(df.index.name)