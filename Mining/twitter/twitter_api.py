import twitter
import pprint 
import json
import os

# Twitter authentification

auth = twitter.oauth.OAuth( os.environ['OAUTH_TOKEN'], 
                            os.environ['OAUTH_TOKEN_SECRET'],
                            os.environ['CONSUMER_KEY'], 
                            os.environ['CONSUMER_SECRET'] )


class TwitterApi(twitter.Twitter):

    def __init__(self, auth):
        self.loglevel=1
        super(TwitterApi, self).__init__(auth=auth)
        
    def get_tweets(self, query, nbatches=10, count=100):
        tweets = []
        search_results = twitter_api.search.tweets(q=query, 
                                                   count=count)
        tweets = search_results['statuses']
        if self.loglevel>1:
            print_search(search_results)
        nsearches = 1
        while True:
            if self.loglevel>0:
                print 'retrieved', len(tweets), 'tweets' 
            if nsearches==nbatches:
                break
            max_id = search_results['search_metadata']['max_id']
            search_results = twitter_api.search.tweets(q=query, count=count, max_id=max_id)
            if self.loglevel>1:
                print_search(search_results)
            newtweets = search_results['statuses']
            tweets += search_results['statuses']
            nsearches += 1 
        return tweets 
        
# twitter_api = twitter.Twitter(auth=auth)
twitter_api = TwitterApi(auth=auth)
 

# YAHOO Where On Earth ID's

WORLD_WOE_ID = 1
US_WOE_ID = 23424977
FR_WOE_ID = 23424819


# some debug functions 

def repr_tweet(tweet):
    return '     '.join( [tweet['id_str'], tweet['text']] )

def print_search(search_results):
    jdump( search_results['search_metadata'] ) 
    tweets =  search_results['statuses']
    print len( tweets )
    jdump([ repr_tweet(t) for t in tweets ]) 

def jdump( val ): 
    '''Just a shortcut'''
    print json.dumps( val, indent=1 )

    
if __name__ == '__main__':

    tweets = twitter_api.get_tweets('#Suisses', nbatches=10)

