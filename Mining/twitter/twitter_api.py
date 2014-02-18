import twitter
import os

auth = twitter.oauth.OAuth( os.environ['OAUTH_TOKEN'], 
                            os.environ['OAUTH_TOKEN_SECRET'],
                            os.environ['CONSUMER_KEY'], 
                            os.environ['CONSUMER_SECRET'] )

def oauth_login():
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

print 'initializing twitter API'
twitter_api = oauth_login()
