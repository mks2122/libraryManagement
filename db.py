import sqlite3
import csv
conn = sqlite3.connect('library.db')
cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS currentDetails")
cur.execute("CREATE TABLE IF NOT EXISTS currentDetails (bookID TEXT PRIMARY KEY, title TEXT, isbn13 TEXT, Name TEXT, Roll TEXT, DueDate TEXT, Status TEXT)")
cur.execute(" INSERT INTO currentDetails (bookID, title, isbn13, Name, Roll, DueDate, Status) VALUES ('1', 'Harry Potter and the Half-Blood Prince', '9780439785969', 'Karthick Sriram', '22AM241', '02-2024', 'Borrowed')")
cur.execute(" INSERT INTO currentDetails (bookID, title, isbn13, Name, Roll, DueDate, Status) VALUES ('21320','Ultimate Spider-Man  Volume 16: Deadpool','9780785119272', 'Allair Joshua', '22AM102', '10-2023', 'Returned')")
# with open('books.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     data = list(reader)
#     cur.execute('''CREATE TABLE IF NOT EXISTS books (
#         bookID TEXT PRIMARY KEY,
#         title TEXT,
#         authors TEXT,
#         isbn TEXT,
#         isbn13 TEXT   )''')
#     for row in data:
#         # print((row))
#         # break
#         cur.execute("INSERT INTO books (bookID,title,authors,isbn,isbn13) values (?, ?,?,?,?)", row)

cur.execute("SELECT * FROM currentDetails")

result = cur.fetchall()
for i in result:
    print(i)
conn.commit()
conn.close()

# import pandas as pd

# df = pd.read_csv('books.csv')

# print(df.head())