import numbers

def validate_input(n):
    if not isinstance(n, numbers.Integral):
        raise ValueError( 'n has to be an integer' )
    if n<0:
        raise ValueError( 'n should be positive' )    

def factorial_iterative(n):
    validate_input(n)
    val = n
    res = 1
    while val>0:
        res *= val
        val -= 1 
    return res


def factorial_recursive(n):
    validate_input(n)
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


if __name__ == '__main__':

    test_values = [0, 1, 2, 3]
    for val in test_values:
        print '{val}! = {res1} {res2}'.format(
            val = val,
            res1 = factorial_iterative(val),
            res2 = factorial_recursive(val) )

    print 'the following should fail'
    try: 
        factorial_recursive(1.5)
    except ValueError as err:
        print err
    try:
        factorial_recursive(-1)
    except ValueError as err:
        print err
