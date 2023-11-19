import pymysql as sql
import pandas as pd

df = pd.read_csv("../HOPE_CSV.csv")

df[df['Regn Num'].str.startswith("22AM")]

df.drop(df[df["Regn Num"].str.startswith("22AM")].index, inplace = True)

data = df[["Regn Num","Name"]].values

len(data)

connection = sql.connect(
    host="localhost",
    user="root",
    password="Kausik@2204",
    db='library'
)

cursor = connection.cursor()

for i in data:
    cursor.execute("INSERT INTO student(ROLL, NAME) VALUES(%s, %s)",(i[0],i[1]))
    connection.commit()git filter-repo --path "*.csv" --prune-empty --tag-name-filter cat -- --all
