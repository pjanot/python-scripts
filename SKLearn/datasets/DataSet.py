import sqlite3
import numpy as np
    
def load_sql( db_filename, table_name, target_name ):
    allowed_vtypes = ['int', 'real']

    # initialize db connection
    print db_filename, target_name
    conn = sqlite3.connect( db_filename )
    c = conn.cursor()
    
    # get column information
    table_info = c.execute('PRAGMA table_info("ads")').fetchall()
    feature_names = []
    other_names = []
    for col_info in table_info:
        idx, name, vtype = col_info[:3]
        if vtype not in allowed_vtypes:
            other_names.append(name)
        elif name != target_name:
            feature_names.append(name)
    print 'features  :', feature_names
    print 'other vars:', other_names
    raws = c.execute('SELECT {vars} FROM {table_name}'.format(
        vars = ','.join(feature_names),
        table_name=table_name) 
        )
    data = np.array(raws.fetchall())
    print data

    raws = c.execute('SELECT {vars} FROM {table_name}'.format(
        vars = ','.join(other_names),
        table_name=table_name) 
        )
    other_data = np.array(raws.fetchall())
    print other_data
    raws = c.execute('SELECT {target_name} FROM {table_name}'.format(
        target_name = target_name,
        table_name = table_name) 
        )
    target = np.array(raws.fetchall()).ravel()
    print target_name
    print target
   
    
    dataset = dict(
        target_names = [target_name],
        target = target, 
        feature_names = feature_names, 
        data = data,
        other_names = other_names,
        other_data = other_data
        )
    return dataset
    
if __name__ == '__main__':

    import sys
    if len(sys.argv)!=4:
        print 'usage: Dataset.py <sqlite db file name> <table name> <name of the target feature>'
        sys.exit(1)
    db_filename, table_name, target_name = sys.argv[1:]
    dataset = load_sql(db_filename, table_name, target_name)

    
