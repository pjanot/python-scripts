
from linkedlist import Node, build_list, print_list

def revert(root):
    parent = None
    node = root
    child = root.child
    while 1:
        # reverting
        node.child = parent
        # one more step
        parent = node
        node = child
        if child is None:
            break
        else:
            child = child.child
    return parent


if __name__ == '__main__':

    import pprint 
    root = build_list()
    print_list(root)

    newroot = revert(root)
    print_list(newroot)
