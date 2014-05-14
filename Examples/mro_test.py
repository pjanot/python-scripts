class Shape(object):
    pass


class Rectangle(Shape):
    pass


class Square(Rectangle):
    pass


class Color(object):
    pass


class RGB(Color):
    pass


class Blue(RGB):
    pass


class BlueSquare(Square, Blue):
    pass


import pprint
pprint.pprint( BlueSquare.__mro__ ) 

## In [10]: %run mro_test.py
## (<class '__main__.BlueSquare'>,
##  <class '__main__.Square'>,
##  <class '__main__.Rectangle'>,
##  <class '__main__.Shape'>,
##  <class '__main__.Blue'>,
##  <class '__main__.RGB'>,
##  <class '__main__.Color'>,
##  <type 'object'>)
