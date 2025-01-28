import sqlite3
con = sqlite3.connect('./TEST.db')
cur = con.cursor()

cur.execute('INSERT INTO TestTable(Date, GetUp) values("2025-01-28", "07:30:00")')
cur.execute('INSERT INTO TestTable(Date, GetUp) values("2025-01-28", "07:30:00")')
cur.execute('INSERT INTO TestTable(Date, GetUp) values("2025-01-28", "07:30:00")')

cur.execute('SELECT * FROM TestTable')
print(cur.fetchall())

con.close()