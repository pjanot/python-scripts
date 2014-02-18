import twitter
import pprint 
import json
import time
import os

auth = twitter.oauth.OAuth( os.environ['OAUTH_TOKEN'], 
                            os.environ['OAUTH_TOKEN_SECRET'],
                            os.environ['CONSUMER_KEY'], 
                            os.environ['CONSUMER_SECRET'] )

def oauth_login():
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api


class RestTwitterApi(twitter.Twitter):

    def __init__(self, twitter_api):
        self.loglevel=1
        self.throttle_count = 0
        self.api = twitter_api
        
        
    def throttle(self, domain='search', operation='/search/tweets',
                 ncall_margin=10):
        '''check if we are about to get rate limited. 
        If the number of remaining calls is less than ncall_margin, wait for nsec.
        '''
        # probably would like to decorate all search functions with this method.
        # if we want a margin of 20, we have to have a shorter period. 
        period = ncall_margin / 2
        print self.throttle_count, period, ncall_margin
        if self.throttle_count%period != 0:
            self.throttle_count += 1
            return  
        # there is also a rate limit on the query below.
        rl = self.api.application.rate_limit_status(resources=domain)
        data = rl['resources'][domain][operation]
        remaining = data['remaining']
        reset_time = data['reset']
        time_to_wait = reset_time - time.time() + 1
        print 'Throttling:', remaining, 'calls remaining. Reset in', time_to_wait, 'seconds.'            
        if remaining <= ncall_margin:
            print 'close to rate limit.. waiting', time_to_wait, 'seconds'
            time.sleep( reset_time - time.time() )
        else: 
            self.throttle_count += 1
            return 

                
    def get_tweets(self, query, nbatches=10, count=100):
        '''Retrieve nbatches of count tweets following query.
        '''
        # the logic here could be reused.
        # looks like twitter now limits at 99. weird
        nbatches = int(nbatches)
        count = int(count)
        tweets = []
        if nbatches < 1: 
            return tweets
        try:
            # why do I get only 99 tweets instead of 100 today? 
            search_results = self.api.search.tweets(q=query, 
                                                count=count)
            tweets = search_results['statuses']
            if self.loglevel>1:
                print_search(search_results)
            nsearches = 1
            while True:
                self.throttle()
                if self.loglevel>0:
                    print '{nsearches}/{nbatches} : {ntweets} tweets'.format(
                        nsearches = nsearches,
                        nbatches = nbatches, 
                        ntweets = len(tweets)
                        ) 
                if nsearches==nbatches:
                    break
                try:
                    next_results = search_results['search_metadata']['next_results']
                    unpck = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
                    kwargs = dict( q=query, count=count, max_id=unpck['max_id']) 
                    search_results = self.api.search.tweets( **kwargs )
                    if self.loglevel>1:
                        print_search(search_results)
                    newtweets = search_results['statuses']
                    tweets += search_results['statuses']
                    nsearches += 1
                except KeyError:
                    print 'no more results'
                    break
        except twitter.TwitterHTTPError, err:
            # would also like to catch ctrl-C
            # we don't want to throw away the tweets collected so far. 
            print 'TwitterHTTPError caught:'
            print  err
        except KeyboardInterrupt: 
            pass
        return tweets 
        
twitter_api = oauth_login()    
rest_twitter_api = RestTwitterApi( oauth_login() )
 
# YAHOO Where On Earth ID's

WOE_IDs = dict(
    WORLD = 1,
    US = 23424977,
    FRANCE = 23424819,
    )

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

    import sys 
    import shelve 
    
    print sys.argv
    hashtag = sys.argv[1]
    nbatches = sys.argv[2]
    tweets = rest_twitter_api.get_tweets(hashtag, nbatches=nbatches)

    output = shelve.open('tweets.shv')
    output['tweets'] = tweets
    output.close()
