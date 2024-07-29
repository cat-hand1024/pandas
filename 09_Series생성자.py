import pandas as pd

data=[80,90,100,95]
indexData=['Kim','Yoon','Choi','Park']

# index 없이 생성
sr=pd.Series(data)
print(sr)

# index 없이 자료형 지정
sr=pd.Series(data,dtype='float')
print(sr)

# index 지정
sr=pd.Series(data,index=indexData)
print(sr)

# dict를 통한 생성
dataDict=dict(zip(indexData,data))
print(dataDict)
sr=pd.Series(dataDict)
print(sr)
