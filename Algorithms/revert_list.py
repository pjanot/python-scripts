
from linkedlist import Node, build_list, print_list

def revert_iterative(root):
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


def revert_recursive(root, parent):
    newroot = None
    if root.child:
        newroot = revert_recursive(root.child, root)
    else:
        newroot = root
    root.child = parent
    return newroot
    
if __name__ == '__main__':

    import pprint 
    root = build_list()
    print_list(root)
    print
    
    newroot = revert_iterative(root)
    print_list(newroot)
    print

    newroot = revert_recursive(newroot, None)
    print_list(newroot)
    print
