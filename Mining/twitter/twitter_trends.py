import sys 
import json
from twitter_api import twitter_api, WOE_IDs

woe_id = WOE_IDs['WORLD']
if len(sys.argv)==2:
    woe_id = WOE_IDs[sys.argv[1]]

world_trends = twitter_api.trends.place(_id=woe_id)
print json.dumps(world_trends, indent=1)

