import time


def throttle(func):
    def inner(*args, **kwargs): 
        nsec = 1
        print 'waiting', nsec
        time.sleep(nsec)
        func(*args, **kwargs)
    return inner

@throttle
def printText(text):
    print text



class throttleWithArguments(object):

    def __init__(self, *args, **kwargs):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print 'init decorator object'
        self.args = args
        self.kwargs = kwargs
        print 'non-keyword args', self.args
        print 'keyword args', self.args

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print "calling decorator"
        def wrapped_f(*args, **kwargs):
            print "Decorator arguments:"
            print self.args
            print self.kwargs
            return f(*args, **kwargs)
        return wrapped_f


@throttleWithArguments(123, 'foo', test='bar')
def printText2(text):
    print text
    
print 'done decorating'
print printText2
    

def printText3(text):
    print text

throttleInstance = throttleWithArguments(blah=1)
printText3 = throttleInstance(printText3)

print 'done decorating manually'
print printText3
   
if __name__ == '__main__':

    # printText('colin')
    # print
    print 
    printText2('colin')
    print
    printText2('Bernet')
