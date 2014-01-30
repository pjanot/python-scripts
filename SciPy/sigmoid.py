import numpy as np
import matplotlib.pyplot as plt
# from math import exp
from scipy.stats import bernoulli 

def sigmoid(x): 
    return 1/(1+np.exp(-x))

X = np.linspace(-10,10,100)

def plot(x):
    plt.clf()
    plt.plot(x, sigmoid(x), label='sigmoid')
    plt.legend(loc=4)
    plt.scatter( x, bernoulli.rvs( sigmoid(x) ) )
    fig = plt.figure(1)
    fig.savefig('sigmoid.pdf')


