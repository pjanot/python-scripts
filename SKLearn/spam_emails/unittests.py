from train import *
from collections import Counter 

import unittest
import shelve

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'set up '
        shlf = shelve.open('output.dat') 
        cls.all_mails = shlf['mails']

    def test_load_data(self):
        '''checks that the data and the labels can be loaded from the mail collection
        and that the resulting iterables have the same size.
        '''
        res, count_vec = load_data(self.__class__.all_mails)
        labels = load_labels( self.__class__.all_mails )
        self.assertEqual( res.shape[0], labels.shape[0] )

    def test_load_labels(self):
        '''checks that:
        - the label is either 0 or 1.
        - the samples are balanced (not more than 70% of samples of a given class)
        '''
        labels = load_labels( self.__class__.all_mails )
        values = set(labels)
        self.assertSetEqual( values, set([0,1]) )
        counter = Counter(labels)
        for count in counter.values():
            frac = float(count) / len(labels)
            self.assertLess( frac, 0.7 )

    ## def test_shuffle(self):
    ##     # make sure the shuffled sequence does not lose any elements
    ##     random.shuffle(self.seq)
    ##     self.seq.sort()
    ##     self.assertEqual(self.seq, range(10))

    ##     # should raise an exception for an immutable sequence
    ##     self.assertRaises(TypeError, random.shuffle, (1,2,3))

    ## def test_choice(self):
    ##     element = random.choice(self.seq)
    ##     self.assertTrue(element in self.seq)

    ## def test_sample(self):
    ##     with self.assertRaises(ValueError):
    ##         random.sample(self.seq, 20)
    ##     for element in random.sample(self.seq, 5):
    ##         self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()
    
