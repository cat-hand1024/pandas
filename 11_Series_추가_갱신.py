import pandas as pd

ID=[1900101,1900102,1900103,1900104]
name=['Kim','Yoon','Choi','Park']

sr=pd.Series(data=ID,index=name)
print(sr)

sr['Yoon']=1900100 # 갱신
sr['Lee']=1900200 # 추가
print(sr)
del sr['Kim'] # 삭제
print(sr)

print(sr['Park']) # 참조
