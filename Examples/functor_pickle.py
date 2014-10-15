import shelve
import sys

class Functor(object):
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, x):
        return self.factor*x


if sys.argv[1] == 'write':
    func = Functor(2)
    print func(3)
    shelf = shelve.open('obj.shelf')
    shelf['func'] = func
    shelf.close()
else:
    shelf = shelve.open('obj.shelf')
    func = shelf['func']
    print func(4)
