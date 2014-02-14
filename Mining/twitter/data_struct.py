import pandas as pd
from dataset import DataSet
from collections import namedtuple
from twitter_api import jdump

# I need to be able to see the tweet text: 
pd.set_option('max_colwidth',200)


'''
Data structure definition for twitter analysis 

Tweet:
    created_at (date of creation)
    lexicographical diversity
    entities  - how to store them? 
      hashtags 
      urls
      user_mentions
    favorite_count
    id (signed int64) or id_str
    retweet_count
    retweeted_status - how to store that? 
      id of original tweet? 
    text
    user (id?)

User
    id
    name 
    following 
    followers 


Need dictionary-like classes to prepare the dataframe inputs. 
namedtuple? or more precisely a list of namedtuples? 
or simply dictionary of arrays? of Series? 
    
'''


class Tweet( namedtuple('Tweet',
                        [ 'id',
                          'retweet_count',
                          'favorite_count',
                          'text'] ) ):
    
    def __new__(cls, tweetjson):
        
        tjs = tweetjson
        kw = dict()

        # stupid twitter stream api doesn't set retweet_count and favorite_count correctly
        retweet_count = 0 
        favorite_count = 0
        retweeted_status = tjs.get('retweeted_status')
        if retweeted_status:
            retweet_count = retweeted_status['retweet_count']
            favorite_count = retweeted_status['favorite_count']
        kw['retweet_count'] = retweet_count
        kw['favorite_count'] = favorite_count 

        kw['id'] = tjs['id'] 
        kw['text'] = tjs['text']
        
        self = super(Tweet, cls).__new__(cls, **kw)
        return self
 

if __name__ == '__main__':

    import json
  
    tset = DataSet( Tweet._fields )
    infile = open('tweets_stream.json')
    for elem in json.load(infile):
        tset += Tweet(elem)

    df = pd.DataFrame(tset)

    
