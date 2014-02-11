import twitter
import pprint 
import json
import os

# Twitter authentification

auth = twitter.oauth.OAuth( os.environ['OAUTH_TOKEN'], 
                            os.environ['OAUTH_TOKEN_SECRET'],
                            os.environ['CONSUMER_KEY'], 
                            os.environ['CONSUMER_SECRET'] )

twitter_api = twitter.Twitter(auth=auth)


# YAHOO Where On Earth ID's

WORLD_WOE_ID = 1
US_WOE_ID = 23424977
FR_WOE_ID = 23424819


def jdump( val ): 
    '''Just a shortcut'''
    print json.dumps( fr_trends, indent=1 )

if __name__ == '__main__':

    fr_trends = twitter_api.trends.place(_id=FR_WOE_ID)
    jdump(fr_trends)
