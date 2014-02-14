import twitter
import shelve
import json
import sys

from oauth import twitter_api
from data_struct import Tweet, DataSet
import pandas as pd

print twitter_api

twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

stream = None
if len(sys.argv)==2:
    q = sys.argv[1]
    stream = twitter_stream.statuses.filter(track=q)
else: 
    # getting a small sample of all public tweets
    stream = twitter_stream.statuses.sample()

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

with open('tweets_stream.json', 'w') as outfile:
  json.dump(tweets, outfile)

df = pd.DataFrame(ds)
