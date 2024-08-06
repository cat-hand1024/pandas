import pandas as pd

file='.\data\easySample2.csv'

df=pd.read_csv(file)

# single position -> Series or 스칼라 리턴
# single index

sr01=df.iloc[2] # 2번째 index 전체

print(sr01)

# single column

sr02=df.iloc[:,1] # columns 1 -> pname 전체
print(sr02)

# single index, single column
scaraValue=df.iloc[1,2] # index 1 / column 2( birth) 스칼라값
print(scaraValue)

# multi position -> DataFrame 반납
# list
df1=df.iloc[[1,2,2],:]
print(df1)
#slice
df2=df.iloc[::2,:] # 짝수만 추출
print(df2)
df3=df.iloc[1::2,:]# 홀수만 추출
print(df3)
