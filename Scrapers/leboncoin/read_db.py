import sqlite3
import sys
import pprint
import webbrowser

args = sys.argv[1:]
table_name = 'ads'

if len(args)!=1:
    print 'usage: read_db.py <sqlite_file.db>'
    sys.exit(1)

db_filename = args[0]

print 'file ', db_filename
print 'table', table_name
print 

conn = sqlite3.connect( db_filename )
cursor = conn.cursor()
table_info = cursor.execute('PRAGMA table_info({table_name})'.format(table_name=table_name)).fetchall()
pprint.pprint( table_info )


zipcodes_dest = dict(
    meximieux = 1800,
    montluel = 1120,
    villieu = 1450,
    st_andre_de_corcy = 1390, # tramoyes, etc
    neyron = 1700, # miribel, beynost, etc.
    )

# select_str = 'SELECT * FROM ads'
select_str = "SELECT * FROM ads WHERE price<1400 AND surface>100 AND date > '2014-03-15' ORDER BY date"
rows = cursor.execute( select_str ).fetchall()


srows = [r for r in rows if r[0] in zipcodes_dest.values() ]
# srows = rows 

for row in srows:
    # print row
    zip, npieces, price, surface, date, url = row
    print 'date', date, 'code_postal =', zip, 'prix =', price, 'Npieces =', npieces, 'surface =', surface
    print url
    print 
    webbrowser.open( url, 2 )
    

