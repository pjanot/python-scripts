from random import randint


def rand7():
    num = 999
    while num > 20:
        num = (randint(1,5) - 1)*5 + randint(1,5) - 1 # between 0 and 24
    return int( num / 3 ) + 1 

