import copy

def permutations_1( words, word, remaining ):
    '''first working attempt.
    words: resulting words (result)
    word:  word in the current stack frame
    remaining: letters remaining in the current stack frame.
      for each of them, a new word is created, and the function
      is recursively called.
    when no letter remains, the current word is appended to the list of words.

    problems:
      list is O(n) for item removal
      copies?
      code could be simplified? 
    ''' 
    if len(remaining) == 0:
        words.append( word )
    for item in remaining:
        newremaining = copy.copy(remaining)
        newremaining.remove(item)
        newword = copy.copy(word)
        newword += item
        permutations( words, newword, newremaining )



 



if __name__ == '__main__':
    iterable = list( 'xxx' )
    words = []
    permutations_1( words, [], iterable)
    print [''.join(word) for word in words]
