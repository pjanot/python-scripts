import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


from sklearn.mixture import GMM


class GenCluster(object):
    
    def __init__(self, mean, width, nsamples=100):
        self.mean = mean
        self.covar = [[width,0],[0,width]]
        self.samples = np.random.multivariate_normal(self.mean,
                                                     self.covar,
                                                     nsamples)        
    def draw(self, color='b'):
        plt.scatter( self.samples[:,0], self.samples[:,1], c=color)



class Gaussian(object):

    def __init__(self, mean, sigma):
        self.mean = mean
        self.sigma = sigma

    def draw(self, color='b'):
        self.c1 = plt.Circle( self.mean, self.sigma,
                              fc=color, ec=color, lw=2, alpha=0.2)
        self.c2 = plt.Circle( self.mean, 2*self.sigma,
                              fc=color, ec=color, lw=2, alpha=0.1)
        plt.gcf().gca().add_artist(self.c1)
        plt.gcf().gca().add_artist(self.c2)
        
    def __str__(self):
        print 'gaussian', self.mean, self.sigma

        

class Event(object):

    def __init__(self):
        self.clusters = []
        self.gmm = None

    def draw(self):
        self.fig = plt.figure(figsize=(10,10))
        colors = 'rbgcm'
        for i, cluster in enumerate(self.clusters):
            color = colors[ i % len(colors) ]
            cluster.draw(color)
        if self.gmm:
            for icircle in range(self.gmm.n_components):
                mean = self.gmm.means_[icircle]
                covar = self.gmm.covars_[icircle]
                sigma = np.sqrt(covar[0])
                g = Gaussian(mean, sigma)           
                g.draw()

    def reconstruct(self, nclusters=None):
        if nclusters is None:
            nclusters = len(self.clusters)
        self.gmm = GMM(n_components=nclusters,
                       covariance_type='spherical',
                       init_params='wc', n_iter=10)
        self.gmm.fit( self.samples )
    
        
    
class SimEvent(Event):

    def __init__(self, means):
        super(SimEvent, self).__init__()
        self.simulate(means)
        self.reconstruct()
        self.draw()
    
    def simulate(self, means):
        self.clusters = [GenCluster(mean,0.2) for mean in means] 
        self.samples = np.concatenate( [cluster.samples for cluster in self.clusters] )





simulator = SimEvent(
     [[-2,-2], [0,0], [2,1], [2,2]]
     )
