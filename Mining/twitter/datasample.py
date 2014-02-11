from collections import OrderedDict
import pandas as pd
    
class DataSet( OrderedDict ):
    
    def __init__(self, fields):
        # not sure I want to declare the fields here.
        # might want to do it at class level
        # maybe there is no big deal. profile
        super(DataSet, self).__init__(self)
        self._fields = tuple( fields )
        for f in self._fields:
            self.setdefault( f, [])

    def __iadd__(self, namedtuple):
        if self._fields != namedtuple._fields:
            errmsg = '''
            trying to add namedtuple with fields:
              {tuplef}
            to DataSet with fields
              {dsf} 
            '''.format(tuplef=namedtuple._fields,                     
                       dsf=self._fields)
            raise ValueError(errmsg)
        # can I do something more elegant? 
        for field in self._fields:
            self[field].append( getattr(namedtuple, field) )           
        return self
    
    def __str__(self):
        thestr = self.repr()
        return thestr

    def __repr__(self):
        repr = 'Dataset: {fields}'.format(fields=str(self._fields))
        return repr
        
if __name__ == '__main__':

    import pprint 
    from collections import namedtuple
    import numpy as np
    
    ds = DataSet(['var1', 'var2', 'var3'])
    
    Row1 = namedtuple('Row1', ['var1', 'var2', 'var3'])

    nentries = 1000000
    for idx in range(nentries):
        if idx%1000 == 0:
            print idx
        v1 = 1 * np.random.randn() + 1
        v2 = 2 * np.random.randn() + 2
        v3 = 3 * np.random.randn() + 3     
        row1 = Row1(v1, v2, v3)
        ds += row1

    df = pd.DataFrame(ds)
        
    # Row2 = namedtuple('Row2', ['v1', 'var2', 'var3'])
    # r2 = Row2(1, 2, 3)
    # this should fail
    # ds += r2
