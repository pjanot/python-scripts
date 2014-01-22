import sqlite3

conn = sqlite3.connect( 'db.txt' )
c = conn.cursor()
raws = c.execute('SELECT * FROM ads')
for r in raws: 
    print r

