import numpy as np

from collections import Counter
import itertools

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn import svm

from sklearn import metrics
from sklearn import cross_validation
from sklearn.utils import shuffle

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

# try:
# - use learning theory to bound the classification efficiency from the training efficiency
# - use cross validation
# - implement unit tests

# would need more control. now a bit like a black box.
# want to be able to follow a sample from the beginning to the end,
# especially during preprocessing. 

def load_data( mails ):
    count_vec = CountVectorizer(
        encoding='iso-8859-1',  # latin 1
        max_df=0.7              # remove words that are present in more than
                                # 70% of the documents
        ) 
    word_lists = [ mail['body'] + mail['sub'] for mail in mails ]
    result = count_vec.fit_transform( word_lists )
    return result, count_vec

def load_labels( mails ):
    labels = np.array( [ mail['label'] for mail in mails] ) 
    return labels


def perf_report(clf, data, target):
    # instantaneous!
    print 'eval...'
    predicted = clf.predict(data)
    train_eff = np.mean( predicted == target)
    print 'training efficiency:', train_eff

    target_names = ['spam', 'not_spam']
    print
    print 'full report:'
    print(metrics.classification_report(target, predicted,
                                        target_names=target_names))

    print
    print 'confusion matrix (0:spam, 1:not spam)'
    print metrics.confusion_matrix(target, predicted)
    
    return train_eff
    

def fit_eval(clf, test_size=0.4):
    '''Fit and evaluate the model.
    prints a report and returns the training efficiency.
    '''
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(
        data, target, test_size=test_size, random_state=4213)

    print 'fit...'
    clf.fit(X_train, y_train)

    if test_size > 0.:
        print 'TEST SAMPLE'
        perf_report(clf, X_test, y_test)
        print
    print 'TRAINING SAMPLE'
    perf_report(clf, X_train, y_train)
    print

    print '5-fold cross-validation...'
    scores = cross_validation.cross_val_score( clf, data, target, cv=5)
    print scores
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

if __name__ == '__main__':

    import sys
    import shelve

    args = sys.argv[1:]
    if len(args)!=1:
        print 'usage: train.py <shelve file with emails>'
        sys.exit(1)
    shlf = shelve.open( args[0] )
    all_mails = shlf['mails']

    use_tf = False
    use_idf = False

    data, counter = load_data(all_mails)
    if use_tf:
        tf_transformer = TfidfTransformer(use_idf=use_idf).fit(data)
        data = tf_transformer.transform(data)

    
    target = load_labels(all_mails) 
    
    assert( len(target) == data.shape[0] )


    # clf = MultinomialNB()
    # clf = SGDClassifier(loss='hinge', penalty='l2',
    #                     alpha=1e-3, n_iter=5)
    clf = svm.SVC( kernel='linear')
    fit_eval(clf)

