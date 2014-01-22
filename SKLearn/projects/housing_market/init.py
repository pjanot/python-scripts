from SKLearn.datasets.DataSet import load_sql

if __name__ == '__main__':

    import sys
    if len(sys.argv)!=4:
        print 'usage: Dataset.py <sqlite db file name> <table name> <name of the target feature>'
        sys.exit(1)
    db_filename, table_name, target_name = sys.argv[1:]
    dataset = load_sql(db_filename, table_name, target_name)

    X = dataset['data']
    y = dataset['target']
    mask =  (X[:,1]<10) & (X[:,2]<500.) & (y[:]<1e6)
    Xr = X[mask]
    yr = y[mask]

    zipcodes = np.unique(Xr[:,0])
    
    plt.hist2d( Xr[:,2], yr, bins=[30,30])
    # plt.scatter( Xr[:,2], yr, c=Xr[:,0]) 

    
