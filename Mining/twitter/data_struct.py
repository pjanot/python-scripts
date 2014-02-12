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

# could this be a slots in the Tweet class? What's a slot btw? 
tweet_fields = [
    'id',
    'retweet_count',
    'favorite_count',
    'text'
    ]

class Tweet( namedtuple('Tweet',tweet_fields) ):

    def __new__(cls, tweetjson):
        args = [ tweetjson[field] for field in cls._fields]
        self = super(Tweet, cls).__new__(cls, *args)
        return self
 

if __name__ == '__main__':

    import shelve
    
    s = shelve.open('tweets.s')
    tweets = s['suisses']
    jdump(tweets[0])

    tset = DataSet( Tweet._fields )

    for tweet in tweets: 
        tset += Tweet(tweet)

    df = pd.DataFrame(tset)
