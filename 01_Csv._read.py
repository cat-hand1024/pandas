import pandas as pd
import os


if __name__=="__main__":

    # data 파일 경로
    path=r"C:\유튜브\pandas\data"
    fileName="easySample.csv"
    file=os.path.join(path,fileName)

    df=pd.read_csv(file,index_col='ID')

    print("INDEX 출력")
    print(df.index) # index는 속성

    print("COLUMNS 출력")
    print(df.columns)

    print('VALUES 출력')
    print(df.values)