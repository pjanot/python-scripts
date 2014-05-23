import numpy as np


class DrawableSample(object):

    def draw(self, color):
        plt.scatter( self.samples[:,0], self.samples[:,1], c=color)



class GenCluster(DrawableSample):

    def __init__(self, mean, width, nsamples=100):
        self.mean = mean
        self.covar = [[width,0],[0,width]]
        self.samples = np.random.multivariate_normal(self.mean,
                                                     self.covar,
                                                     nsamples)
    ## def draw(self, color='b'):
    ##     plt.scatter( self.samples[:,0], self.samples[:,1], c=color)



class Simulator(DrawableSample):
    def __init__(self, means, width):
        self.clusters = []
        self.samples = None
        self.simulate_clusters(means, width)

    def simulate_clusters(self, means, width):
        self.clusters = [GenCluster(mean, width) for mean in means]
        samples = [cluster.samples for
                   cluster in self.clusters]
        self.samples = np.concatenate(samples)



if __name__ == '__main__':

    simulator = Simulator([[-2,-2], [0,0], [2,1], [2,2]], 0.2)
