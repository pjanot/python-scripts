import twitter
import shelve
import json
import sys

from twitter_api import twitter_api
from data_struct import Tweet, DataSet
import pandas as pd

print twitter_api

twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

def init_stream(query='', outfile='tweets_stream.json', language='en'):   
    stream = None
    if query!='':
        stream = twitter_stream.statuses.filter(track=query,
                                                language=language)
    else: 
        # getting a small sample of all public tweets
        stream = twitter_stream.statuses.sample(language=language)

    tweets = []
    ds = DataSet( Tweet._fields )
    try:
        for tweet in stream:
            if tweet.get('delete'): 
                # tweet deletions?
                continue
            tweets.append( tweet )
            dtw = Tweet(tweet)
            print dtw
            ds += dtw
            sys.stdout.flush()
    except KeyboardInterrupt:
        pass

    with open(outfile, 'w') as outfile:
        json.dump(tweets, outfile)
        df = pd.DataFrame(ds)
    return tweets, df

if __name__ == '__main__':

    query = ','.join(sys.argv[1:])
    tweets, df = init_stream( query, language='fr' )  
