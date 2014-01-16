from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
from sklearn import neighbors

cmap_bold = ['#FF0000', '#00FF00', '#0000FF']
lcmap_bold = ListedColormap(cmap_bold)

lcmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])

h = 0.02

def train_test(data, target, ntest): 
    data_train, data_test = np.split( data, [-ntest])
    target_train, target_test = np.split( target, [-ntest]) 
    return data_train, target_train, data_test, target_test
    
def sort_truth(x, truth):
    assert(len(x)==len(truth))
    categs = np.unique(truth)
    sorted_events = []
    for categ in categs:
        # print categ
        mask = (truth==categ)
        # print mask
        sorted_events.append( x[mask] )
    return sorted_events    



def plot_var(x, truth, nbins):
    plt.clf()
    x_by_categs = sort_truth(x, truth)
    plt.hist(x_by_categs, nbins)
    

def plot_correlation(ix, iy, data, truth):
    '''plot: 
    - the y vs x 
    - each point is coloured according to truth, if given
    - the x, y plane is painted according to the results of the classifier
    ''' 

    # what does this do exactly? 
    # I'm getting several windows, but I'd like to clear the existing one. 
    plt.clf()
    knn = neighbors.KNeighborsClassifier()
    knn.fit( data[:,[ix,iy]], truth)

    x = data[:,ix]
    y = data[:,iy]
    
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    # x and y coordinates for each point on the grid
    # linspace instead of arange?
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    # after ravel, both xx and yy are 1D.
    # putting together these 1D arrays:
    # array([[ 3.3 , -0.9 ],
    #        [ 3.32, -0.9 ],
    #        [ 3.34, -0.9 ],
    #   ..., 

    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

    # now go back to the 2D matrix
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=lcmap_light)

    plt.scatter(x, y, c=truth, cmap=lcmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())


if __name__ == '__main__':
    from sklearn import datasets
    
    iris = datasets.load_iris()
    
