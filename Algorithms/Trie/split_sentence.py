from trie import Trie, build_dict_trie

dtrie = build_dict_trie()

## dtrie = Trie()
## dtrie.insert('pea')
## dtrie.insert('nut')
## dtrie.insert('peanut')
## dtrie.insert('butter')
## dtrie.insert('butt')

def split_sentence(words, sentence="peanutbutter"):
    if len(sentence)<2:
        return
    word=''
    imax = None
    for i, letter in enumerate(sentence):
        word += letter
        # next, the problem is that I start from scratch everytime.
        # there is probably a way to go down the branch of the trie
        sub = dtrie.subtrie(word)
        if sub and sub.is_valid():
            # print 'word exists:', word, i+1
            imax = i+1
        # else:
        #    print 'cannot find:', word
    #store the biggest word on the left,
    #and split the remaining part on the right
    words.append( sentence[:imax])
    split_sentence(words, sentence[imax:])

def split(sentence):
    words = []
    split_sentence(words, sentence)
    print words
