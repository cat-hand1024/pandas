import pandas as pd

def change_weekdayText(row):
    weekNum=[0,1,2,3,4,5,6]
    weekText=['월','화','수','목','금','토','일']
    weekNum_To_Text=dict(zip(weekNum,weekText))
    return weekNum_To_Text[row.day_of_week]

file='.\data\easySample2.csv'

df=pd.read_csv(file)

df=df[['pname','birth']]

df['birth']=pd.to_datetime(df['birth']) # 07_DataFrame_to_datetime

df01=df.copy()
df02=df.copy()

df['year']=df['birth'].dt.year
# 생일이 1992년인 사람 출력
print(df[df['year']==1992])

# 생일 요일 출력

# 1. datetime의 dt.weekday -> 요일 표시
weekNum = [0, 1, 2, 3, 4, 5, 6]
weekText = ['월', '화', '수', '목', '금', '토', '일']
weekNum_To_Text = dict(zip(weekNum, weekText))
df01['요일']=df01['birth'].dt.weekday
df01['요일']=df01['요일'].replace(weekNum_To_Text)
print(df01)

# timedelta -> 요일 표시
df02['요일']=df02['birth'].apply(change_weekdayText)
print(df02)

