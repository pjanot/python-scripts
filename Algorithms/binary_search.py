
def binary_search( sequence, element ): 
    smin = 0
    smax = len(sequence)
    while smax>smin: 
        midpoint = smin + (smax - smin)/2
        print smin, midpoint, smax
        if element > sequence[midpoint]:
            smin = midpoint+1 
        elif element < sequence[midpoint]:
            smax = midpoint
        else:
            return midpoint

if __name__ == '__main__':

    import sys

    element = int( sys.argv[1] )
    sequence = range(100000000)

    # print element
    # print sequence
    index = binary_search(sequence, element ) 
    print 'resulting index', index
