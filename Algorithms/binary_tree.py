import pprint
import unittest 

class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_children(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        left = 'null'
        right = 'null'
        if self.left:
            left = self.left.value
        if self.right:
            right = self.right.value
        return str('node: {val} {left} {right}'.format(val = self.value,
                                                       left = left,
                                                       right = right ) )


def dfs_inorder_recursive(node):
    return []

def dfs_inorder_iterative(node):
    return []

def dfs_morris(node):
    return []


class TreeTestCase( unittest.TestCase ):

    def setUp(self):
        self.nodes = dict( (i, Node(i) ) for i in range(6) )
        self.nodes[4].set_children( self.nodes[2], self.nodes[5] )
        self.nodes[2].set_children( self.nodes[0], self.nodes[3] )
        self.nodes[0].right = self.nodes[1]
        self.root = self.nodes[4]

    def test_tree_structure(self):
        self.assertMultiLineEqual(
            pprint.pformat(self.nodes),
            '{0: node: 0 null 1,\n 1: node: 1 null null,\n 2: node: 2 0 3,\n 3: node: 3 null null,\n 4: node: 4 2 5,\n 5: node: 5 null null}')

    def test_dfs_inorder_recursive(self):
        result = dfs_inorder_recursive( self.root )
        self.assertEqual(result, range(6) )

    def test_dfs_inorder_iterative(self):
        result = dfs_inorder_iterative( self.root )
        self.assertEqual(result, range(6) )

    def test_dfs_morris(self):
        result = dfs_morris( self.root )
        self.assertEqual(result, range(6) )


if __name__ == '__main__':
    unittest.main()
