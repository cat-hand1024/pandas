import pandas as pd

file='.\data\easySample2.csv'

df=pd.read_csv(file)

df['overtime']=pd.to_timedelta(df['overtime'])

# timedelta 타입은 days,seconds로만 변환 가능
print(df['overtime'].dt.seconds)

# 시간 전환 : 1시간은 3600초
df['minute'],df['second']=divmod(df['overtime'].dt.seconds,60)  # 전체 second은 minuter과 second로 나눔
df['hour'],df['minute']=divmod(df['minute'],60) # 나누어진 분을 시간과 분으로 나눔

print(df[['hour','minute','second']])

# 10시간 이상 근무자 출력하기
print(df[df['hour']>10])

