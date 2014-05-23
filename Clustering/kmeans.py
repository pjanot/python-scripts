import unittest
import numpy as np


def distance_1(x1, x2):
    '''Linear distance.'''
    return np.linalg.norm(x1-x2)

def distance_2(x1, x2):
    '''Quadratic distance.'''
    return np.sum( (x1-x2)**2 )

def distance_manhattan(x1, x2):
    '''sum of the distances along each axis.'''
    return np.sum( np.abs( x1-x2 ) )



class KMeans( object ):

    def __init__(self, samples, centroids, distance):
        self.centroids = centroids.astype('float')
        self.samples = samples.astype('float')
        self.distance = distance
        self.clusterids = np.zeros( len(self.samples) )
        self.dispersion = 0.

    def fit(self):
        niter = 0
        while 1:
            self.associate_()
            dispersion = self.update_()
            print dispersion
            if abs(dispersion - self.dispersion)<1e-9:
                print 'converged in ', niter, 'iteration(s).'
                break
            else:
                self.dispersion = dispersion
                niter += 1

    def associate_(self):
        '''associate each sample to a cluster'''
        for isam, sample in enumerate(self.samples):
            min_dist = 1e9
            for icent, centroid in enumerate(self.centroids):
                dist = self.distance( sample, centroid)
                if dist<min_dist:
                    min_dist = dist
                    self.clusterids[isam] = icent

    def update_(self):
        '''recompute cluster position'''
        dispersion = 0.
        for icent, _ in enumerate(self.centroids):
            associated_samples = self.samples[ self.clusterids==icent ]
            newpos = np.mean( associated_samples, axis=0)
            self.centroids[icent] = newpos
            dists = distance_2( associated_samples, newpos )
            dispersion += np.sum(dists)
        return dispersion


class Test_KMeans(unittest.TestCase):

    def setUp(self):
        self.samples = np.array([[0.,0.],
                                 [0.,1.],
                                 [1.,1.],
                                 [0.,-1.],
                                 [2.,2.]])

    def test_distance_1(self):
        self.assertEqual( distance_1(self.samples[0], self.samples[1]), 1 )
        self.assertEqual( distance_1(self.samples[0], self.samples[2]), np.sqrt(2) )
        self.assertEqual( distance_1(self.samples[0], self.samples[3]), 1 )
        self.assertEqual( distance_1(self.samples[0], self.samples[4]), np.sqrt(8) )

    def test_distance_manhattan(self):
        self.assertEqual( distance_manhattan(self.samples[0], self.samples[1]), 1 )
        self.assertEqual( distance_manhattan(self.samples[0], self.samples[2]), 2 )
        self.assertEqual( distance_manhattan(self.samples[0], self.samples[3]), 1 )
        self.assertEqual( distance_manhattan(self.samples[0], self.samples[4]), 4 )


    def test_distance_2(self):
        self.assertEqual( distance_2(self.samples[0], self.samples[1]), 1 )
        self.assertEqual( distance_2(self.samples[0], self.samples[2]), 2 )
        self.assertEqual( distance_2(self.samples[0], self.samples[3]), 1 )
        self.assertEqual( distance_2(self.samples[0], self.samples[4]), 8 )

    def test_associate_update(self):
        centroids = np.array([[-1.,-1.],
                              [2., 1.]] )
        kmeans = KMeans(self.samples, centroids, distance_1)
        kmeans.associate_()
        self.assertTrue( np.all( kmeans.clusterids ==
                                 [ 0.,  1.,  1.,  0.,  1.] ) )
        kmeans.update_()
        # print kmeans.centroids
        # print kmeans.dispersion

    def test_dispersion(self):
        samples = np.array([[0.,0],
                            [1.,0],
                            [3.,3],
                            [3.,4]])
        centroids = np.array([[0.,0], [3.,3]])
        kmeans = KMeans(samples, centroids, distance_1)
        kmeans.associate_()
        dispersion = kmeans.update_()
        self.assertEqual(dispersion, 1)

    def test_fit_simple(self):
        samples = np.array([[0.,0],
                            [1.,0],
                            [3.,3],
                            [3.,4]])
        centroids = np.array([[0.,0], [3.,3]])
        kmeans = KMeans(samples, centroids, distance_1)
        kmeans.fit()
        self.assertTrue(True)

    def test_fit_real(self):
        pass

if __name__ == '__main__':

    unittest.main()
