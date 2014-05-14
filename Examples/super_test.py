# http://rhettinger.wordpress.com/2011/05/26/super-considered-super/

import pprint

class Root(object):

    ## def __init__(self, **kwds):
    ##     # just in case arguments are left unused,
    ##     # stripping them off.
    ## not sure this is proper design. if the user provides an argument
    ## that is not planned by the system, one wants to get a TypeError
    ## TypeError: object.__init__() takes no parameters
    ##     super(Root,self).__init__()
        
    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(Root, self), 'draw')


class Shape(Root):
    '''
    For reorderable method calls to work, the classes need to be designed cooperatively. This presents three easily solved practical issues:

    - the method being called by super() needs to exist
    - the caller and callee need to have a matching argument signature
    - and every occurrence of the method needs to use super()

    '''
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        print 'Shape constructor:'
        pprint.pprint(kwds)
        super(Shape, self).__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super(Shape, self).draw()

class Color(Root):
    def __init__(self, color, **kwds):
        self.color = color
        print 'Color constructor:'
        pprint.pprint(kwds)
        super(Color, self).__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super(Color, self).draw()


class AlienShape(object):
    '''not cooperative, maybe a class imported from another system.
    if after Root in the MRO, will fire the assertion in Root.draw
    ''' 
    def draw(self):
        print '''
        AlienShape.draw.
        This method is masked by Root.draw if AlienShape after Root in the MRO.
        If it is before, it does not delegate Shape.draw.
        So in any case, it is completely useless,
        hence the assertion in Root.draw
        '''
        print 


class ColoredShape1(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        print 'ColoredShape1 constructor:'
        pprint.pprint(kwds)
        super(ColoredShape1, self).__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super(ColoredShape1, self).draw()



class ColoredShape(Color, Shape):
    '''
    The only purpose of this class is to decide about the mro:
    the color is initialized and drawn before the shape.
    Color and Shape are exchangeable! 
    '''
    pass


class ShapedColor(Shape, Color):
    pass



class AlienShapeAdapter(Root):
    '''
    Adapts the external class AlienShape,
    so it can be used collaboratively.
    '''
    def __init__(self, **kwargs):
        self.alien = AlienShape()
        super(AlienShapeAdapter,self).__init__(**kwargs)
        
    def draw(self):
        self.alien.draw()
        super(AlienShapeAdapter,self).draw()
        

class ColoredAlienShape(AlienShapeAdapter, Color):
    pass


pprint.pprint( ColoredShape1.__mro__ ) 
print

cs1 = ColoredShape1(color='blue', shapename='square')
cs1.draw()

print 

cs = ColoredShape(color='blue', shapename='square')
cs.draw()

print 

sc = ShapedColor(color='blue', shapename='square')
sc.draw()

print

cas = ColoredAlienShape(color='blue')
cas.draw()
