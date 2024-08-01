import pandas as pd

ID=[1900101,1900102,1900103,1900104]
columns=['Name','English','Chines','Korean']

name=['Kim','Yoon','Choi','Park']
english=[80,90,100,95]
chines=[100,80,70,85]
korean=[95,100,80,60]

# list 생성 -> 각 리스트를 쌓아올리는 방식
df=pd.DataFrame(data=[name,english,chines,korean])
print(df)
df=pd.DataFrame(data=[name,english,chines,korean],columns=ID,index=columns)
print(df)

data_dict=dict(zip(columns,[name,english,chines,korean]))
print(data_dict)
df=pd.DataFrame(data=data_dict)
print(df)

