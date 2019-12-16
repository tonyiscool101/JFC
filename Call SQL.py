import sqlite3

conn = sqlite3.connect('Bigboy.db')


c = conn.cursor()
t = ('IBM',)
c.execute('SELECT * FROM IDList WHERE ID=?', t)
print(c.fetchone())