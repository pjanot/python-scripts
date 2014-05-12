
def fibonacci_recursive_1(n, val=1, pre=0, level=2):
    ''' n >= 0
    0 -> 0
    1 -> 1
    2 -> 1
    3 -> 2
    ...
    
    This is my first solution. single branch stack!

    level indicates the index at which we have the value val.
    pre is the value before that.
    
    we go up in the number of levels until
    we hit level n. we take the value obtained there,
    and rewind the stack, returning this value everytime. 
    '''
    # print level, pre, val
    if n<0:
        raise ValueError('n must be >= 0.')
    elif n==0:
        return 0
    elif n==1:
        return 1
    elif level<n:
        return fibonacci_recursive_1(n, val+pre, val, level+1)
    else: # level=n
        return val+pre

def fibonacci_recursive_2(n):
    '''
    Double-branch stack, going the other way round, towards 0.
    much more simple, but the stack is branching at each level.
    do i care?
    yes, this function takes ages for n>30!
    '''
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_recursive_2(n-1) + fibonacci_recursive_2(n-2) 


def fibonacci_iterative(n):
    '''
    much easier for the brain and the processor.
    '''
    val = 1
    pre = 0
    if n<0:
        raise ValueError('n must be >= 0.')        
    if n==0:
        return pre
    if n==1:
        return val
    else:
        i = 2
        while i<=n:
            val, pre = val+pre, val
            i+=1
        return val

        
if __name__ == '__main__':

    fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    print 'n\ttrue\tpred'
    for i, val in enumerate(fibo):
        print i, '\t', val, '\t', fibonacci_iterative(i)

    
