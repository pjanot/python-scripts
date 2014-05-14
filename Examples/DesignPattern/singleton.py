
class Foo(object):
    def __init__(self):
        print 'creating Foo', id(self)


class Singleton(object):
    theFoo = Foo()

    def foo(self):
        return self.__class__.theFoo
    

if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    


