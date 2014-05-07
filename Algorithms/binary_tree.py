import pprint
import unittest 
from stack import stack 


class Node(object):
    '''
    There is no need for a Tree class. In fact the Node is equivalent
    to the subtree rooted at this node.
    '''
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def visit(self):
        return self.value

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


def dfs_inorder_recursive(node, result):
    if node is None:
        return 
    dfs_inorder_recursive(node.left, result)
    result.append( node.visit() )
    dfs_inorder_recursive(node.right, result)


def dfs_preorder_recursive(node, result):
    if node is None:
        return 
    result.append( node.visit() )
    dfs_preorder_recursive(node.left, result)
    dfs_preorder_recursive(node.right, result)


def dfs_preorder_iterative(root, result):
    todo = stack()
    todo.append(root)
    while len(todo):
        node = todo.pop()
        if node.right:
            todo.append(node.right)
        if node.left:
            todo.append(node.left)
        result.append( node.value )


def dfs_inorder_iterative(root, result):
    to_visit = stack()
    to_visit.append(root)
    node = root
    n = 0
    while len(to_visit):
        print node 
        if node.right:
            to_visit.append( node.right )
        to_visit.append( node )
        if node.left:
            to_visit.append( node.left )
        if node.right is None or (node.right.value == to_visit.peek().value):
            result.append( node.value )
            node = to_visit.pop()
        node = to_visit.pop()

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

    # can I avoid this boilerplate code with decorators? 
    def test_dfs_inorder_recursive(self):
        result = []
        dfs_inorder_recursive( self.root, result )
        self.assertEqual(result, range(6) )

    def test_dfs_preorder_recursive(self):
        result = []
        dfs_preorder_recursive( self.root, result )
        self.assertEqual(result, [4, 2, 0, 1, 3, 5] )

    def test_dfs_preorder_iterative(self):
        result = []
        dfs_preorder_iterative( self.root, result )
        self.assertEqual(result, [4, 2, 0, 1, 3, 5] )

    ## def test_dfs_inorder_iterative(self):
    ##     result = []
    ##     dfs_inorder_iterative( self.root, result )
    ##     self.assertEqual(result, range(6) )

    ## def test_dfs_morris(self):
    ##     result = dfs_morris( self.root )
    ##     self.assertEqual(result, range(6) )


if __name__ == '__main__':
    unittest.main()
