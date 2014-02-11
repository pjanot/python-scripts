import pandas as pd

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

    

if __name__ == '__main__':

    test_data_1 = dict( col1 = [0,1,2,2], col2 = ['a','b','c', 'c'])
    test_data_2 = dict( col1 = [0,1,2,2], col2 = ['a','b','c', 'c'])
    
    test_df = pd.DataFrame(test_data_1)
    print test_df
    print 'drop duplicates'
    print test_df.drop_duplicates()

