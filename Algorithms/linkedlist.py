
class Node(object):

    def __init__(self, value):
        self.child = None
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __iter__(self):
        yield self.child


def iterate(node):
    while node is not None:
        yield node
        node = node.child


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


def print_list(root):
    while root:
        print root, '->', root.child
        root = root.child


if __name__ == '__main__':

    import pprint
    root = build_list()
    print_list(root)

    for node in iterate(root):
        print node
