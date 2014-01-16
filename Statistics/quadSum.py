from math import sqrt

def quadSum( values ):
    sum = 0.
    for v in values:
        fv = float(v)
        sum += fv*fv
    return sqrt(sum)

if __name__ == '__main__':

    import sys

    vals = sys.argv[1:]
    print quadSum(vals)
