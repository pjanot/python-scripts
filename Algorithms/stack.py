
def error( fun ):
    def wrapper( *args, **kwargs ):
        print 'sorry, call is not allowed'
    return wrapper


# maybe a metaclass is a better solution than a decorator?

class Stack(list):

    # the error function can be used as a manual decorator
    __getitem__ = error( list.__getitem__ )

    __delitem__ = error( list.__delitem__ )

    # or using the decorator syntactic sugar
    @error
    def remove(self, item):
        pass

    @error
    def insert(self, index, object):
        pass


if __name__ == '__main__':

    stack = Stack()
    stack.append(1)
    stack[0]
    stack.remove(1)
    stack.append(2)
    del stack[0]
    stack.insert(0, 5)
    stack.pop()
    print stack 
