from SKLearn.datasets.DataSet import load_sql
from sklearn import datasets, linear_model

def plot_feature( feat_array, target_array ):
    plt.clf()
    plt.hist2d( feat_array, target_array, bins=[30,30])
    clf = linear_model.LinearRegression()
    clf.fit(feat_array[:,np.newaxis], yr)
    print 'fitted model: {a} X + {b}'.format(
        a = clf.coef_[0],
        b = clf.intercept_
        ) 
    # x grid
    px = np.linspace(0, 500)
    px = px[:,np.newaxis] # need an array with shape n_samples, 1
    plt.plot(px, clf.predict(px), color='yellow', linewidth=3)
    

def plot_class_pdg(X, y):
    '''
    X : design matrix
    y : target true classes
    ''' 
    plt.clf()
    plt.hist2d( feat_array, target_array, bins=[30,30])

    logit = linear_model.LogisticRegression()
    logit.fit(X, y)
 
    
    
if __name__ == '__main__':

    import sys
    if len(sys.argv)!=4:
        print 'usage: Dataset.py <sqlite db file name> <table name> <name of the target feature>'
        sys.exit(1)
    db_filename, table_name, target_name = sys.argv[1:]
    dataset = load_sql(db_filename, table_name, target_name)

    X = dataset['data']
    y = dataset['target']

    # less than 10 rooms, 500 m2, and 1 million euros
    mask =  (X[:,1]<10) & (X[:,2]<500.) & (y[:]<1e6)
    Xr = X[mask]
    yr = y[mask]

    zipcodes = np.unique(Xr[:,0])
    
    plot_feature(Xr[:,2], yr)

    file_paysdegex = open('communes_pays_de_gex_filtered.txt')
    zips_pdg = []
    for line in file_paysdegex:
        zipcode = line.split()[-1]
        zips_pdg.append(float(zipcode))

    ispdgr = np.array([False]*len(yr))
    for i, data in enumerate(Xr):
        zipcode = data[0]
        if zipcode in zips_pdg:
            ispdgr[i] = True 

    plt.scatter( Xr[ispdgr,2], yr[ispdgr], c='r')
    plt.scatter( Xr[!ispdgr,2], yr[!ispdgr], c='w')

    #for classification between pays de gex or not, 
    #prepare samples with the same number of events
    yvsx = np.array([Xr[:, 2], yr ]).T
    yvsx_notpdg = yvsx[ ispdgr==False ][:309]
    yvsx_pdg = yvsx[ispdgr]
    X_norm = np.vstack( [yvsx_pdg, yvsx_notpdg] )
    y_norm  = np.array([np.ones(309), np.zeros(309)]).ravel()
    logit = linear_model.LogisticRegression()
    logit.fit(X_norm, y_norm)
    print 'not pdg', logit.predict([100., 150000])
    print 'pdg', logit.predict([100., 400000])

    # set up cross validation and 2D display!
    # after confirming that the model is working on the normalized samples, 
    # - try to see if there is a way to avoid normalization before the fact
    # - or write some code to normalize properly in a reproducible way.
    # add the number of rooms feature, and see if the classification improves
    
    
