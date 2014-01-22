import sqlite3
import time

conn = sqlite3.connect( 'db.txt' )
c = conn.cursor()
# Create table
try:
    c.execute('''CREATE TABLE ads
      (zipcode int, npieces int, price real, surface real, url text)
    ''')
    conn.commit()
except sqlite3.OperationalError:
    # database already created
    pass


qry = "INSERT INTO ads VALUES ({zipcode},{npieces},{price},{surface},'{url}')".format(
        zipcode = 1,
        npieces = 2,
        price = 3,
        surface = 4,
        url = 'url',
)
print qry
c.execute(qry)
conn.commit()

time.sleep(20)
