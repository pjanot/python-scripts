
class stack(object):
    '''
    Does not inherit from list because i want to restrict the interface
    to the bare minimum.

    Methods:
    append
    pop
    peek
    __len__
    '''

    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append( item )

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def __len__(self):
        return len(self.items)



import unittest

class TestStack(unittest.TestCase):

    def test_stack(self):
        s = stack()
        s.append(1)
        s.append(2)
        s.append(3)
        self.assertEqual( s.peek(), 3)
        self.assertEqual( s.pop(), 3)
        self.assertEqual( s.peek(), 2)
        s.pop()
        s.pop()
        self.assertEqual( len(s), 0 )
        

if __name__ == '__main__':
    unittest.main()
