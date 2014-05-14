class A(object):
    '''
    If __new__ doesn't return an instance of the class it's bound to (e.g. GimmeFive), it skips the Constructor Step entirely.
    '''
    def __new__(cls):
        return super(A,cls).__new__(B)
    def __init__(self):
        self.name = "A"

class B(object):
    def __new__(cls):
        return super(B,cls).__new__(A)
    def __init__(self):
        self.name = "B"
        
a = A()
print type(a), hasattr(a, 'name')
