import pandas as pd
import pymysql as sql

df = pd.read_csv("../AML A Database.csv")
df2 = pd.read_csv("../AML B Database.csv")
data = df[["ROLL NO","NAME","EMAIL ID"]].values.tolist()

connection = sql.connect(
    host="localhost",
    user="root",
    password="Kausik@2204",
    db='library'
)
cursor = connection.cursor()
for i in data:
    try:
        cursor.execute("INSERT INTO student(ROLL, NAME) VALUES(%s, %s)",(i[0],i[1]))
        connection.commit()
    except sql.IntegrityError as e:
        pass

#Converting all names in NAME column to upper case
df['NAME'] = df['NAME'].str.upper()


bdf = pd.read_csv("../../data/2nd Year Database B.csv")
bdf['NAME'] = df['NAME'].str.upper()
data = df[["ROLL NO","NAME"]].values.tolist()
for i in data:
    try:
        cursor.execute("INSERT INTO student(ROLL, NAME) VALUES(%s, %s)",(i[0],i[1]))
        connection.commit()
    except sql.IntegrityError as e:
        pass