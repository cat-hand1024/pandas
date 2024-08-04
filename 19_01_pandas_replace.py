import pandas as pd


sr=pd.Series([1,2,3,4,5])

df=pd.DataFrame({
                    'A':[0,1,2,3,4],
                    'B':[5,6,7,8,9],
                    'C':['1,000','2,000','3,000','4,000','5,000']}
)

# 스칼라 변경

print(sr)
print(sr.replace(1,5)) # 1을 5로 변환

print(df)
print(df.replace(0,5)) # 0을 5로 변환



# list 변경
print(df.replace([0,1,2,3],10)) # 0,1,2,3을 10으로

# dict 변경
print(df.replace({0:10,1:100,2:1000}))

#정규식 변경

print(df.replace(',','',regex=True)) # 천단위 콤마 삭제
