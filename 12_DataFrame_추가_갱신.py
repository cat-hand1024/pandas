import pandas as pd

ID=[1900101,1900102,1900103,1900104]
columns=['Name','English','Chines','Korean']

name=['Kim','Yoon','Choi','Park']
english=[80,90,100,95]
chines=[100,80,70,85]
korean=[95,100,80,60]


data_dict=dict(zip(columns,[name,english,chines,korean]))

df=pd.DataFrame(data_dict)
print(df)

df['korea']=[100]*4 # 갱신
df['france']=[100,80,70,85] # 추가

print(df)