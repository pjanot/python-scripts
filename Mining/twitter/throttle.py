import time
from twitter_api import twitter_api

class throttle(object):
    '''Throttling decorator for twitter API calls.

    Use like this:

    @throttle('search', '/search/tweets')
    def your_function(text):
        ...
    '''
    
    def __init__(self, domain, operation):
        self.domain = domain
        self.operation = operation
        self.call_count = 0
        self.ncall_margin = 10

        self.test = False
        
    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            period = self.ncall_margin - 1
            # print period, self.call_count
            if self.call_count%period != 0:
                self.call_count += 1
                return func(*args, **kwargs)
                return  
            # there is also a rate limit on the query below.
            remaining = 999
            reset_time = time.time() + 999.
            if not self.test:
                rl = twitter_api.application.rate_limit_status(resources=self.domain)
                data = rl['resources'][self.domain][self.operation]
                remaining = data['remaining']
                reset_time = data['reset']
            time_to_wait = reset_time - time.time() + 1
            print 'Throttling:', remaining, 'calls remaining. Reset in', time_to_wait, 'seconds.'            
            if remaining <= self.ncall_margin:
                print 'close to rate limit.. waiting', time_to_wait, 'seconds'
                time.sleep( reset_time - time.time() )
            self.call_count += 1
            return func(*args, **kwargs)
        return wrapped_func


if __name__ == '__main__':


    @throttle('search', '/search/tweets')
    def hello(text):
        print 'hello', text

    # hello('world')
    for i in range(15):
        print i
        hello('colin')
