import numpy as np

# weight functions

def identity(x, x0=None): 
    '''Uniform weighting, doesn't depend on the position of x0.'''
    return np.ones_like(x) 

def gaussian(x, x0): 
    '''Gaussian weighting according to the distance between x and x0.''' 
    deltas = (x0 -x)
    # is there a way to do that without the python loop? 
    d2 = np.array([ v.dot(v) for v in deltas ])
    d2 = d2[:, np.newaxis]
    tau2 = 1
    weights = np.exp( -d2 / (2*tau2) )
    return weights 

def zfun(x, y, w, theta):
    return w * ( y - sigmoid( x.dot(theta) ))      


def newtonIteration( x, y, theta, weights, lambdapar=0.0001):
    hyptheta = sigmoid( x.dot( theta ) ) 
    zs = weights * (y - hyptheta)
    
    # gradient of the log likelihood
    gradll = x.T.dot( zs ) - lambdapar * theta 
    
    # D matrix
    ds = -weights*hyptheta*(1-hyptheta)
    D = np.diag( ds.ravel() ) 
    
    # hessian H = XT D X - Lambda I 
    idty = np.identity(theta.shape[0])
    H =  x.T.dot( D.dot(x) ) - lambdapar * idty
    
    # inverse of the hessian
    Hinv = np.linalg.inv(H)
    
    theta = theta - Hinv.dot( gradll )
    return theta     

def chi2(x, y, theta): 
    # 0.5 (x theta -y)T. (x theta - y)
    dist = x.dot(theta) - y  
    res = dist.T.dot(dist)
    assert(res.shape == (1,1))
    return res[0][0]

# --- 

def sigmoid(z): 
    '''logistic function'''
    return 1 / (1+np.exp(-z))
    
def addInterceptColumn(x): 
    newshape = x.shape[0], x.shape[1]+1
    newx = np.ones( newshape )
    newx[:, 1:] = x
    return newx
   


class LogisticRegression( object ): 

    def __init__(self, x, y ):
        '''
        x = 2D array of shape m x k where
           m is the number of samples
           k is the number of features
        y = 1D array of shape m, 
           containing boolean values describing 
           whether a given sample is accepted or rejected 
        '''

        self.weight = gaussian
        self.lambdapar = 0.0001

        # initializing parameters to 1
        self.theta = np.zeros( x.shape[1] +1 ) # +1 for the intercept
        self.theta = self.theta[:, np.newaxis]
        self.x = addInterceptColumn(x)
        self.y = y[:, np.newaxis]
        # self.ycol = y[:, np.newaxis]

        
    def fit(self, x0, weight=identity): 
        '''Fit the model.
        x0 = 1D array of shape k for locally weighted logistic regression
        weight = weighting function, by default identity.
        '''
        weights = self.weight(self.x, x0)

        oldchi2 = -1
        newchi2 = 0
        niter = 0
        while abs(newchi2-oldchi2)>0.001:
            self.theta = newtonIteration(self.x, self.y, self.theta, 
                                         weights, self.lambdapar)
            oldchi2 = newchi2
            newchi2 = chi2(self.x, self.y, self.theta)
            niter += 1 
        print 'converged. number of iterations:', niter

        
    def predict(self, x0=None, weight=identity): 
        '''x0 = 1D array of shape k
        returns the boolean prediction of the model for the input sample x0
        '''
        assert( len(x0.shape)==1 )
        x0_icept = np.ones( x0.shape[0]+1 )
        x0_icept[1:] = x0
        if x0:
            self.fit(x0_icept, weight)
 

if __name__ == '__main__':
    
    X = np.array( [[0],
                   [1],
                   [1.2],
                   [1.5],
                   [1.8],
                   [2.0]]
                   )
    y = np.array( [0,0,0,1,1,1] ) 

    lg = LogisticRegression( X, y )
    x0 = np.array([1.2])
    self = lg

    lin = np.linspace(0, 2, 100)
    linx = lin[:,np.newaxis]
    linx = addInterceptColumn(linx)
    # plt.plot( lin, sigmoid( linx.dot( lg.theta ) ) )
    lg.predict(x0)
    plt.plot( lin, sigmoid( linx.dot( lg.theta ) ) )
    # lg.fit(x0)
    # plt.plot( lin, sigmoid( linx.dot( lg.theta ) ) )
    # lg.fit(x0)
    # plt.plot( lin, sigmoid( linx.dot( lg.theta ) ) )
    # lg.fit(x0)
    # plt.plot( lin, sigmoid( linx.dot( lg.theta ) ) )
    # lg.fit(x0)
    # plt.plot( lin, sigmoid( linx.dot( lg.theta ) ) )
    plt.scatter(X, y)
