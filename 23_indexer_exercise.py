import pandas as pd
import numpy as np

file='.\data\easySample2.csv'

df=pd.read_csv(file,index_col='ID')
df.replace({'chinese':r'\s'},{'chinese':np.nan},regex=True,inplace=True)


df=df.astype({'chinese':'float'})
df['birth']=pd.to_datetime(df['birth'])
df['overtime']=pd.to_timedelta(df['overtime'])
df['year']=df['birth'].dt.year
print(df.info())

# 'pname','birth','dept','salary'열 추출
df01=df[['pname','birth','dept','salary']]
print(df01)

# dept='Education' and chinese=1
df02=df.loc[(df['dept']=='Education')&(df['chinese']==1),['pname','dept','chinese']]
print(df02)
# 생일이 1992년인 자로 출력 ( birth,pname,overtime)
df03=df.loc[df['year']==1992,['birth','pname','overtime']]
print(df03)

# index가 19로 시작하고 dept가 'Marketing'인 자료 추출
print(df.loc[(df.index>18999999)&(df['dept']=='Marketing')])

# overtime이 16시간 이상인 pname,dept,overtime 자료 추출
print(df.loc[df['overtime'].dt.seconds//3600>=16,['pname','dept','overtime']])



