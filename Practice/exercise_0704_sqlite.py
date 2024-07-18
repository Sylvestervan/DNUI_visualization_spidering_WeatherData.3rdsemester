import sqlite3


conn = sqlite3.connect('test0704.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
cursor.execute("INSERT INTO stocks VALUES ('2021-05-05', 'BUY', 'RHAT', '100', '35.14')")

conn.commit()
conn.close()

conn = sqlite3.connect('test0704.db')
cursor = conn.cursor()
c = cursor.execute('SELECT * FROM stocks ORDER BY price')
print(c)
for i in c:
    print(i)
conn.close()