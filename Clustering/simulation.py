import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn.mixture import GMM

class Cluster(object):
    def __init__(self, mean, width, nsamples=100):
        self.mean = mean
        self.covar = [[width,0],[0,width]]
        self.samples = np.random.multivariate_normal(self.mean,
                                                     self.covar,
                                                     nsamples)
        
    def draw(self, color='b'):
        plt.scatter( self.samples[:,0], self.samples[:,1], c=color)



class Simulator(object):

    def __init__(self, means):
        self.simulate(means)
        self.reconstruct()
        self.draw()
    
    def simulate(self, means):
        self.clusters = [Cluster(mean,0.2) for mean in means] 
        self.samples = np.concatenate( [cluster.samples for cluster in self.clusters] )

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
                sigma = sqrt(covar[0])
                c1 = plt.Circle( mean, sigma, fc='b', ec='b', lw=2, alpha=0.2)
                c2 = plt.Circle( mean, 2*sigma, fc='b', ec='b', lw=2, alpha=0.1)
                self.fig.gca().add_artist(c1)
                self.fig.gca().add_artist(c2)
                

    def reconstruct(self, nclusters=None):
        if nclusters is None:
            nclusters = len(self.clusters)
        self.gmm = GMM(n_components=nclusters,
                       covariance_type='spherical',
                       init_params='wc', n_iter=10)
        self.gmm.fit( self.samples )


simulator = Simulator(
    [[-2,-2], [0,0], [2,1], [2,2]]
    )
