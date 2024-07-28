import pandas as pd
import os

def check_Unnamed(col_values):
    for check in col_values:
        if 'Unnamed' in check:
            return True
    return False

def change_col(df):
    newHeader=df.iloc[0,:]
    df.columns=newHeader
    return df.iloc[1:,:]

def preProcess_Col(df):
    while True:
        if check_Unnamed(col_values=df.columns.values):
            df=change_col(df=df)
        else:
            return df

# data 파일 경로
path = r"C:\유튜브\pandas\data"
fileName = "element_응용.csv" # Head가 없는 CSV
file = os.path.join(path, fileName)

df=pd.read_csv(file)
df=preProcess_Col(df=df)
print(df)


