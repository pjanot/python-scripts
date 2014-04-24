import numpy as np

from ROOT import TTree

class TreeNumpy(object):
    
    def __init__(self, name, title, defaultFloatType="D", defaultIntType="I"):
        '''Create a tree. 

        attributes:
          tree    the ROOT TTree

        functions:
          var     book a variable
          vector  book an array
          fill    fill a variable
          vfill   fill an array
          reset   reset all variables to their default value
          copyStructure  copy the structure of an existing TTree
        '''
        self.vars = {}
        self.vecvars = {}
        self.tree = TTree(name, title)
        self.defaults = {}
        self.vecdefaults = {}
        self.defaultFloatType = defaultFloatType
        self.defaultIntType = defaultIntType
        
    def copyStructure(self, tree):
        for branch in tree.GetListOfBranches():
            name = branch.GetName() 
            typeName = branch.GetListOfLeaves()[0].GetTypeName()
            type = float
            if typeName == 'Int_t':
                type = int
            self.var(name, type)            
    
    def branch_(self, selfmap, varName, type, len, postfix="", storageType="default", title=None):
        """Backend function used to create scalar and vector branches. 
           Users should call "var" and "vector", not this function directly."""
        if storageType == "default": 
            storageType = self.defaultIntType if type is int else self.defaultFloatType
        if type is float  :
            if storageType == "F": 
                selfmap[varName]=np.zeros(len,np.float32)
                self.tree.Branch(varName,selfmap[varName],varName+postfix+'/F')
            elif storageType == "D":
                selfmap[varName]=np.zeros(len,np.float64)
                self.tree.Branch(varName,selfmap[varName],varName+postfix+'/D')
            else:
                raise RuntimeError, 'Unknown storage type %s for branch %s' % (storageType, varName)
        elif type is int: 
            dtypes = {
                "i" : np.uint32,
                "s" : np.uint16,
                "b" : np.uint8,
                "l" : np.uint64,
                "I" : np.int32,
                "S" : np.int16,
                "B" : np.int8,
                "L" : np.int64,
            }
            if storageType not in dtypes: 
                raise RuntimeError, 'Unknown storage type %s for branch %s' % (storageType, varName)
            selfmap[varName]=np.zeros(len,dtypes[storageType])
            self.tree.Branch(varName,selfmap[varName],varName+postfix+'/I')
        else:
            raise RuntimeError, 'Unknown type %s for branch %s' % (type, varName)
        if title:
            self.tree.GetBranch(varName).SetTitle(title)


    def var(self, varName, type=float, default=-99, title=None, storageType="default" ):
        '''Book a single variable with name varName.

        default is the value to which the variable is initialized if the reset function is called. 
        
        storageType specifies the storage type used for the branch declaration, e.g. 'F', 'D' or 'L'.
        if not specified, the default storageType corresponding to the specified type is used.
        '''
        self.branch_(self.vars, varName, type, 1, title=title, storageType=storageType)
        self.defaults[varName] = default
        

    def vector(self, varName, lenvar, maxlen=None, vtype=float, default=-99, title=None, storageType="default" ):
        """Book a vector variable with name varName.
        
        To book a variable length array,
        lenvar should be the name of the variable containing the size of the array, e.g.:
        tree.var('ndata', int)
        tree.vector( 'data', lenvar='ndata' )

        A fixed length array is booked in the following way: 
        tree.vector( 'data', lenvar=10 )    
        """
        if type(lenvar) == int:  
            self.branch_(self.vecvars, varName, vtype, lenvar, postfix="[%d]" % lenvar,
                         title=title, storageType=storageType)
        else:
            if maxlen == None: RuntimeError, 'You must specify a maxlen if making a dynamic array';
            self.branch_(self.vecvars, varName, vtype, maxlen, postfix="[%s]" % lenvar,
                         title=title, storageType=storageType)
        self.vecdefaults[varName] = default
        

    def reset(self):
        '''Resets all variables to their initialization values.'''
        for name,value in self.vars.iteritems():
            value[0]=self.defaults[name]
        for name,value in self.vecvars.iteritems():
            value.fill(self.vecdefaults[name])

            
    def fill(self, varName, value ):
        '''Fill the variable varName with the value.'''
        self.vars[varName][0]=value

        
    def vfill(self, varName, values ):
        '''Fill the array varName with the values in the iterable.'
        a = self.vecvars[varName]
        for (i,v) in enumerate(values):
            a[i]=v



if __name__=='__main__':
    
    from ROOT import TFile
    from ROOT import gPad

    f = TFile('TreeNumpy.root','RECREATE')
    t = TreeNumpy('Colin', 'Another test tree')
    t.var('a')
    t.var('ndata', int)
    maxlen=100
    t.vector('data', lenvar='ndata', maxlen=maxlen)

    nevents = 10000
    for i in range(nevents):
        t.fill('a', 3)
        ndata = np.random.randint(maxlen) 
        t.fill('ndata', ndata )
        t.vfill('data', range(ndata))
        t.tree.Fill()
    t.tree.Print()
    # t.tree.Scan()
    t.tree.Draw('data>>h(100,0,100)')
    gPad.Update()
    
    # f.Write()
    # f.Close()
    
