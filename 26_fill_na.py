import pandas as pd
import numpy as np

file='.\data\easySample2.csv'

df=pd.read_csv(file,index_col='ID')

# fillna(value=,axis=)

df=df.replace(r'^\s+$',np.nan,regex=True)

df01=df[['english','japanese','chinese']]
print(df01.fillna(value=0))
print(df01.fillna(value={'english':-1,'chinese':2}))