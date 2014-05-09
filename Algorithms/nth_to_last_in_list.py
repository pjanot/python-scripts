
from linkedlist import Node, build_list

def look_ahead(node, n_to_last, thenode):
    if thenode[0]:
        return -1
    n_ahead = 0
    if node.child:
        n_ahead = look_ahead(node.child, n_to_last, thenode)
    if n_ahead == n_to_last:
        thenode[0] = node
        # print 'found', node
    # print n_ahead
    return n_ahead+1


if __name__ == '__main__':

    import pprint 
    root = build_list()

    thenode = [None]
    look_ahead(root, 2, thenode)
    print thenode[0]





