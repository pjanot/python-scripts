import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


# weight functions

def identity(x, x0=None): 
    '''Uniform weighting, doesn't depend on the position of x0.'''
    return np.ones( len(x) )[:,np.newaxis]

def make_gaussian(tau2):
    def gaussian(x, x0): 
        '''Gaussian weighting according to the distance between x and x0.''' 
        deltas = (x0 -x)
        # is there a way to do that without the python loop? 
        d2 = np.array([ v.dot(v) for v in deltas ])
        d2 = d2[:, np.newaxis]
        weights = np.exp( -d2 / (2*tau2) )
        return weights 
    return gaussian


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
    
    # inverse of the hessian ***************
    # if things are done correctly, that's where 
    # we should be spending our time. 
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
    try: 
        return 1 / (1+np.exp(-z))
    except: 
        return 0.
        
def addInterceptColumn(x): 
    newshape = x.shape[0], x.shape[1]+1
    newx = np.ones( newshape )
    newx[:, 1:] = x
    return newx
   


class LogisticRegression( object ): 

    maxiter = 100
    
    def __init__(self, x, y):
        '''
        x = 2D array of shape m x k where
           m is the number of samples
           k is the number of features
        y = 1D array of shape m, 
           containing boolean values describing 
           whether a given sample is accepted or rejected 
        '''
        self.lambdapar = 0.0001
        self.x = addInterceptColumn(x)
        self.y = y[:, np.newaxis]
        self.initialize()
        # self.ycol = y[:, np.newaxis]

    def initialize(self):
        # initializing parameters to 1
        self.theta = np.zeros( self.x.shape[1] )
        self.theta = self.theta[:, np.newaxis]        
        
    def fit(self, x0, weightfun=identity): 
        '''Fit the model.
        x0 = 1D array of shape k for locally weighted logistic regression
        weightfun = weighting function, by default identity.
        '''
        weights = weightfun(self.x, x0)

        oldchi2 = -1
        newchi2 = 0
        niter = 0
        while abs(newchi2-oldchi2)>0.001:
            self.theta = newtonIteration(self.x, self.y, self.theta, 
                                         weights, self.lambdapar)
            oldchi2 = newchi2
            newchi2 = chi2(self.x, self.y, self.theta)
            niter += 1 
            if niter==self.__class__.maxiter:
                print "didn't converge after", niter, 'iterations. EXIT'
                return
            # print 'converged. number of iterations:', niter

        
    def predict(self, x0=None, weightfun=identity): 
        return int(self.score(x0, weightfun)>0.5)

    
    def score(self, x0=None, weightfun=identity):
        '''x0 = 1D array of shape k
        returns the boolean prediction of the model for the input sample x0
        '''
        assert( len(x0.shape)==1 )
        self.initialize()
        x0_icept = np.ones( x0.shape[0]+1 )
        x0_icept[1:] = x0
        if x0 is not None:
            self.fit(x0_icept, weightfun)
        self.prediction = sigmoid( self.theta.T.dot(x0_icept) )
        return self.prediction[0]
    

def simple1DTest():   
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
    return lg



class Dataset(object):
    
    def __init__(self, file_x, file_y): 
        def readvalues(fnam): 
            f = open(fnam)
            vals = []
            for line in f: 
                lvalues = [float(v) for v in line.split()]
                vals.append( lvalues )
            return vals
        self.X = np.array( readvalues(file_x) )
        self.y = np.array( readvalues(file_y) ).flatten()
        print self.X
        print self.y

    def plot(self):
        cm_bright = ListedColormap(['blue', 'yellow'])
        plt.scatter( ds.X[:,0], ds.X[:,1], c=ds.y, cmap=cm_bright)
        
if __name__ == '__main__':
    
    # lg = simple1DTest()

    ds = Dataset('problem_set_1/q1_x.dat', 'problem_set_1/q1_y.dat')
    # ds.plot()

    lg = LogisticRegression( ds.X, ds.y )
    x0 = np.array([7,2])
    gaus2 = make_gaussian(2)
    gaus05 = make_gaussian(0.5)
    gaus02 = make_gaussian(0.2)
    gaus005 = make_gaussian(0.005)

    resol = 50
    xx, yy = np.meshgrid( np.linspace(0, 8, resol), np.linspace(-5, 5, resol))

    # the following line is bad! should be able to use the internal numpy loop.
    #  well how bad is it? maybe I want to profile. 
    # would be interesting 
    # - to mimic the scikit-learn interface
    # - try and use the scikit-learn minimization algorithms, to see if they are faster.

    def plot(fun):
        Z = np.array([ lg.score(point, fun) for point in np.c_[xx.ravel(), yy.ravel()] ])
        Zr = Z.reshape(xx.shape)
        plt.pcolormesh( xx,yy, Zr, cmap=cm.gray)
        ds.plot()

        #     plt.plot( xx, yy, c=Z )
    
    
    # print lg.predict( x0, gaus2)    
