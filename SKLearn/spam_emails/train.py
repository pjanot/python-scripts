from collections import Counter
import itertools

from sklearn.feature_extraction.text import CountVectorizer

# scipy sparse matrices

# some ideas:
# remove very common words - feature available
# remove words that are present less than x times - feature available
# in some cases a header is present (see mail 0) - still need to deal with that
# convert from html to text - done!
# lowercase everything - done! 
# deal with punctuation - done!


# I should test them in a pragmatic way, based on the performance of the classification
# do not overdesign before having a measure of performance.

def preprocess( mail ):
    # here clean up
    words = mail['body'].split()
    mail['words'] =  words
    mail['vocabulary'] = set(words)


## def build_vocabulary( mails ):
##     '''returns the full set of words used in the mails'''
##     vocabulary = set() 
##     for mail in all_mails: 
##         preprocess( mail )
##         vocabulary.update( mail['vocabulary'] ) 
##     return vocabulary
   
## def build_vocabulary2( mails ):
##     '''returns a counter for the full set of words used in the mails.'''
##     word_lists = [ mail['words'] for mail in mails ]
##     vocabulary = Counter( itertools.chain(*word_lists) ) 
##     return vocabulary


def load_mails( mails ):
    count_vec = CountVectorizer(encoding='iso-8859-1') # latin 1 encoding
    word_lists = [ mail['body'] + mail['sub'] for mail in mails ]
    result = count_vec.fit_transform( word_lists )
    return result, count_vec

if __name__ == '__main__':

    import sys
    import shelve

    args = sys.argv[1:]

    if len(args)!=1:
        print 'usage: train.py <shelve file with emails>'
        sys.exit(1)

    shlf = shelve.open( args[0] )
    all_mails = shlf['mails']

    

 
