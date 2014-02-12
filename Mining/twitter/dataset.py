from collections import OrderedDict
import pandas as pd
    
class DataSet( OrderedDict ):
    '''Class holding data before the creation of a dataframe. 

    Example:
    
    import pandas as pd 
    ds = DataSet(['var1', 'var2', 'var3'])
    # ... fill the dataset ...
    df = pd.DataFrame(ds)
    '''
    
    def __init__(self, fields):
        '''Create a dataset, with a list of fields.

        Example: 
        ds = DataSet(['var1', 'var2', 'var3'])

        '''
        # not sure I want to declare the fields here.
        # might want to do it at class level
        # maybe there is no big deal. profile
        super(DataSet, self).__init__(self)
        self._fields = tuple( fields )
        for f in self._fields:
            self.setdefault( f, [])

    def __iadd__(self, namtuple):
        '''Add a row of values from a namedtuple, by doing: 
        The fields must be compatible: namedtuple._fields == self._fields 

        Example:
        Row = namedtuple('Row', ['var1', 'var2', 'var3'])
        row = Row(1.0, 2.0, 'a_label')
        dataset += row

        '''
        if self._fields != namtuple._fields:
            errmsg = '''
            trying to add namtuple with fields:
              {tuplef}
            to DataSet with fields
              {dsf} 
            '''.format(tuplef=namtuple._fields,                     
                       dsf=self._fields)
            raise ValueError(errmsg)
        # can I do something more elegant? 
        for field in self._fields:
            self[field].append( getattr(namtuple, field) )           
        return self
    
    def __repr__(self):
        repr = 'Dataset: {fields}'.format(fields=str(self._fields))
        return repr


    
if __name__ == '__main__':

    import pprint 
    from collections import namedtuple
    import numpy as np
    
    ds = DataSet(['var1', 'var2', 'var3'])
    
    Row1 = namedtuple('Row1', ['var1', 'var2', 'var3'])

    nentries = 50
    for idx in range(nentries):
        if idx%1000 == 0:
            print idx
        v1 = 1 * np.random.randn() + 1
        v2 = idx%2
        v3 = 'unit'
        if idx%10 == 0: 
            v3 = 'ten'
        row1 = Row1(v1, v2, v3)
        ds += row1

    df = pd.DataFrame(ds)
        
    # Row2 = namedtuple('Row2', ['v1', 'var2', 'var3'])
    # r2 = Row2(1, 2, 3)
    # this should fail
    # ds += r2
