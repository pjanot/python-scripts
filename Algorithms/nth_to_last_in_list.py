
class Node(object):
    def __init__(self, value):
        self.child = None
        self.value = value

    def __repr__(self):
        return str(self.value)

def build_list(N=10):
    parent = None
    root = None
    for i in range(N):
        node = Node(i)
        if parent:
            parent.child = node
        else:
            root = node
        parent = node
    return root


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





