class Base(object):
    def __new__(cls):
        '''
        when calling super on an instance, the method
        is bound to the instance, so we do:
        super(Base, self).__init__()
        here we don't have an instance, so we must pass cls to __new__
        '''
        obj = super(Base, cls).__new__(cls)
        print 'create', obj
        return obj

    def __init__(self):
        print 'init', self


a = Base()

