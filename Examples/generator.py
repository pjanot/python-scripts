'''Generator example.
Yields elements in the Fibonacci sequence.
'''

def fibonacci_sequence(pre=0, val=1):
    '''Yields: element in the fibonacci sequence.'''
    while 1:
        yield pre
        val, pre = val+pre, val


if __name__ == '__main__':

    for i, value in enumerate(fibonacci_sequence()):
        print value
        if i == 9:
            break
