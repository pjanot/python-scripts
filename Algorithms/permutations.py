import copy


def permutations_1( perms,
                    remaining_elements, 
                    current_perm = None):
    '''first working attempt.

    problems:
      list is O(n) for item removal...
      really slow...
      copies? yes, profiling shows it's the main issue. 
      not exactly what is asked, but at the same time, it's good
        to have a generic function for any kind of iterable.
    '''
    if current_perm is None:
        current_perm = []
    if len(remaining_elements) == 0:
        perms.append( current_perm )
    for item in remaining_elements:
        new_remaining_elements = copy.copy(remaining_elements)
        new_remaining_elements.remove(item)
        new_current_perm = copy.copy(current_perm)
        new_current_perm += item
        permutations_1( perms,
                        new_remaining_elements,
                        new_current_perm)


def permutations_2( perms,
                    elements,
                    current_perm = None,
                    used = None,
                    level = None):
    '''
    about twice faster, mostly because I eliminated unnecessary copies.  
    note the use of the level and used variables!!
    '''
    if current_perm is None:
        # initialization when first entering the function.
        current_perm = [None] * len(elements)
        used = [False] * len(elements)
        level = 0
    level += 1 
    if level == len(elements):
        # all elements used
        perms.append( current_perm )
    for i, item in enumerate( elements ):
        if used[i]:
            continue
        used[i] = True
        # just a O(1) assignment is enough!
        # the call stack will keep track of each version of current_perm
        current_perm[level-1] = item
        permutations_2( perms,
                        elements,
                        current_perm,
                        used,
                        level)
        # that's clever. again, the right version of used has been
        # passed to the next frame
        used[i] = False



if __name__ == '__main__':
    iterable = list( 'colinsdaf' )
    words = []
    permutations_1( words, iterable )
    print len(words)
#    print [''.join(word) for word in words]


# In [6]: %timeit permutations_1( words, list('colinbern') )
# 1 loops, best of 3: 3.08 s per loop

# In [7]: %timeit permutations_2( words, list('colinbern') )
# 1 loops, best of 3: 1.69 s per loop
