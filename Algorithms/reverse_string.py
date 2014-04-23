def reverse(theStr):
    newStr = []
    for i in range( len(theStr) ):
        newStr.append(theStr[-(i+1)] )
    return ''.join( newStr ) 

if __name__ == '__main__':
    import sys

    print reverse2( sys.argv[1] )
