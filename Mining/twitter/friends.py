from throttle import throttle
from twitter_api import twitter_api
import shelve


class User(object):
    
    def __init__(self, ujson):
        self.ujson = ujson
        self.id = ujson['id']
        self.name = ujson['name'].encode('utf-8', 'replace')
        self.following = []

    def __str__(self):
        return '{id} {name}'.format(id=self.id, name=self.name)


        
@throttle('users', '/users/lookup')
def users_lookup(*args, **kwargs):
    return twitter_api.users.lookup( *args, **kwargs )

@throttle('friends', '/friends/ids', ncall_margin=1)
def friends_ids(*args, **kwargs):
    return twitter_api.friends.ids( *args, **kwargs )



    
class Crawler(object):
    
    def __init__(self):
        self.users = dict()
        self.current = None
        
    def addUser(self, user_id, user_json=None):
        user = self.users.get(user_id, None)
        if user:
            print 'user', str(user), 'is already in the list'
            return True
        if user_json is None:
            user_json  = users_lookup( user_id = user_id )[0]
        user = User( user_json )
        self.users[user_id] = user
        self.current = user

    def addFriends(self, user_id):
        fids = friends_ids(user_id = user_id)['ids']
        user = self.users[user_id]
        user.following = fids
        # print fids
        # adding the first 100 ids.
        users = users_lookup( user_id=','.join( str(id) for id in fids[:100] ))
        for user_json in users:
            user_id = user_json['id']
            self.addUser(user_id, user_json)
        
    def next(self):
        self.current

        

def testCrawl():      
    user_id = 469248037 # Wallerand de St Just        
    crawler = Crawler()
    crawler.addUser(user_id) 
    crawler.addFriends(user_id)
    fids = crawler.users[469248037].following
    for friend_id in fids[:50]:
        crawler.addFriends(friend_id)
    return crawler
        
# insh = shelve.open('graph.shv')
# crawler =  insh['graph']

crawler = testCrawl()

## import networkx as nx

## graph = nx.Graph()
## for user_id, user in crawler.users.iteritems():
##     for friend_id in user.following:
##         graph.add_edge(user_id, friend_id)

## clusters =  nx.clustering(graph)
## for user_id, value in clusters.iteritems():
##     if value<0.001:
##         continue
##     user = crawler.users.get(user_id, None)
##     if user:
##         print user

        
#     # need to do something clean:
#     #  see cookbook chap 9 for catching exceptions
#     #  throttling

#     # how to validate friendship?
#     # e.g. Wallerand follows france inter...
#     # accepted if
#     #    the candidate friend follows N friends?
#     #    other N friends follow the candidate friend
#     #  use an MVA?
