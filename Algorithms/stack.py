'''
Provides a stack class.
'''

class Stack(object):
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
        '''Create empty stack.'''
        self.items = []

    def append(self, item):
        '''Append item on top of the stack.'''
        self.items.append(item)

    def pop(self):
        '''Remove and return last inserted item on top of the stack.'''
        return self.items.pop()

    def peek(self):
        '''Access top of the stack, but do not remove item.'''
        return self.items[-1]

    def __len__(self):
        '''Return the size of the stack.'''
        return len(self.items)



import unittest

class TestStack(unittest.TestCase):
    '''Test case for the Stack class.'''

    def test_stack(self):
        '''Test that the stack behaves as a stack.'''
        stc = Stack()
        stc.append(1)
        stc.append(2)
        stc.append(3)
        self.assertEqual(stc.peek(), 3)
        self.assertEqual(stc.pop(), 3)
        self.assertEqual(stc.peek(), 2)
        stc.pop()
        stc.pop()
        self.assertEqual(len(stc), 0)


if __name__ == '__main__':
    unittest.main()

