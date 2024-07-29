import pandas as pd
import os

def fileName_join(fileName):
    path = r"C:\유튜브\pandas\data"
    file = os.path.join(path, fileName)
    return file


# data 파일 경로

file=fileName_join(fileName= "astype_sample.csv")


df=pd.read_csv(file,index_col='ID')

df['birth']=pd.to_datetime(df['birth'])

df['year']=df['birth'].dt.year
df['month']=df['birth'].dt.month
df['day']=df['birth'].dt.day

df_To_Csv=df[['birth','year','month','day']]
print(df_To_Csv)


# to_csv index=True (default)
file=fileName_join(fileName='saveCsv_indexTrue.csv')
df_To_Csv.to_csv(file,index=True)

# to_Csv index=False
file=fileName_join(fileName='saveCsv_indexFalse.csv')
df_To_Csv.to_csv(file,index=False)

# to_csv header=False ( default -> True )
file=fileName_join(fileName='saveCsv_headerFalse.csv')
df_To_Csv.to_csv(file,header=False)

# to_csv 출력할 컬럼을 지정
file=fileName_join(fileName='saveCsv_choiceCol.csv')
df.to_csv(file,columns=['birth','year','month','day'])
