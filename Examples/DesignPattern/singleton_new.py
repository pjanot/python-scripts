

class Singleton_1(object):
    '''A first try, not working. see Singleton_2'''
    instance = None
    
    def __new__(cls):
        if cls.instance is None:
            print 'creating instance'
            cls.instance = super(Singleton_1, cls).__new__(cls)
        # when putting the return under the if,
        # the object is created only when instance is None.
        # not good. 
        return cls.instance
        
    def __init__(self):
        '''
        executed every time a new object is created
        (every time the instance is accessed).
        not good, as attributes get reinitialized. 
        '''
        print 'initializing instance'
        self.var = 0



class SingletonMeta( type ):

    def __call__(cls, *args, **kwds):
        # print '__call__ of ', str(cls)
        # print '__call__ *args=', str(args)
        if cls.instance is None:
            print 'creating instance'
            cls.instance = type.__call__(cls, *args, **kwds)
        else:
            print 'returning instance'
        return cls.instance
        

class Singleton_2(object):
    '''Yeah!'''
    __metaclass__ = SingletonMeta
    instance = None
    
    def __init__(self):
        print 'initializing instance'
        self.var = 0
    

if __name__ == '__main__':
    Singleton = Singleton_2
    
    a = Singleton()
    a.added = True
    a.var = 1 
    b = Singleton()
    print hex(id(a)), hex(id(b)), b.added, b.var

