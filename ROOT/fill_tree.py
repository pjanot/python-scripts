from ROOT import TTree
import numpy as np

tree = TTree('tree', 'test')

max_size = 10

ndata = 0
data = np.zeros( max_size, dtype=np.float32 )
tree.Branch('ndata', ndata, 'ndata/I' )
tree.Branch('data', data, 'data[{size}]/F'.format(size=max_size) )

nevents = 10

# need an efficient way to copy the data,
# and to clear it. 

for i in range(nevents):
    ndata = i+1
    theData = np.linspace(1, i+1, ndata)
    for j, datum in enumerate(theData): 
        data[j] = datum
    print ndata, '-', data
    tree.Fill()


