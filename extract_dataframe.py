import json
import pandas as pd
from textblob import TextBlob


def read_json(json_file: str)->list:
    """
    json file reader to open and read json files into a list
    Args:
    -----
    json_file: str - path of a json file
    
    Returns
    -------
    length of the json file and a list of json
    """
    
    tweets_data = []
    for tweets in open(json_file,'r'):
        tweets_data.append(json.loads(tweets))
    
    
    return len(tweets_data), tweets_data

class TweetDfExtractor:
    """
    this function will parse tweets json into a pandas dataframe
    
    Return
    ------
    dataframe
    """
    def __init__(self, tweets_list):
        
        self.tweets_list = tweets_list

    # an example function
    def find_statuses_count(self)->list:
        statuses_count = []
        for i in range(len(self.tweets_list)):
            statuses_count.append(self.tweets_list[i]['user']['statuses_count'])
        return statuses_count
        
#     def find_full_text(self, text)->list:
# #         text = text
       
    
    def find_Language(self):
        language = []
        for i in range(len(self.tweets_list)):
            language.append(self.tweets_list[i]['user']['lang'])
        return language
        
        
    def find_created_time(self)->list:
        created_at = []
        for i in range(len(self.tweets_list)):
            created_at.append(self.tweets_list[i]['created_at'])
       
        return created_at

    def find_source(self)->list:
        source = []
        for i in range(len(self.tweets_list)):
            source.append(self.tweets_list[i]['source'])

        return source
    
    def find_followers_count(self)->list:
        followers_count = []
        for i in range(len(self.tweets_list)):
            followers_count.append(self.tweets_list[i]['user']['followers_count'])
            
        return followers_count
    
    def find_friends_count(self)->list:
        friends_count = []
        for i in range(len(self.tweets_list)):
            friends_count.append(self.tweets_list[i]['user']['friends_count'])
            
        return friends_count
    
    def find_favourite_count(self)->list:
        favourite_count = []
        for i in range(len(self.tweets_list)):
            favourite_count.append(self.tweets_list[i]['user']['favourites_count'])
            
        return favourite_count
    
    def find_retweet_count(self)->list:
        retweet_count = []
        for i in range(len(self.tweets_list)):
            retweet_count.append(self.tweets_list[i]['retweet_count'])
            
        return retweet_count
     
        
#     def find_followers_count(self)-->list:
#         full_text = []
#         for i in range(len(self.tweets_list)):
#             full_text.append(self.tweets_list[i]['full_text'])
        
#         return full_text

    def get_tweet_df(self,save = False)->pd.DataFrame:
        
        statuses_count = self.find_statuses_count()
        created_at = self.find_created_time()
        source = self.find_source()
        language = self.find_Language()
        followers_count = self.find_followers_count()
        friends_count = self.find_friends_count()
        favourite_count = self.find_favourite_count()
        retweet_count = self.find_retweet_count()
        
        ll = [created_at,statuses_count,source,language,followers_count,friends_count,favourite_count,retweet_count]
        columns = ['created_at','statuses_count','source','language','followers_count','friends_count','favourite_count','retweet_count']
                          
                   
        df = pd.DataFrame()
        for i in range(len(ll)):
            df[columns[i]] = ll[i]
        
        
        
        
#         df = pd.DataFrame(statuses_count,columns)
# # # #         data = zip(created_at, source, text, polarity, subjectivity, lang, fav_count, retweet_count, screen_name, follower_count, friends_count, sensitivity, hashtags, mentions, location)
# #         df = pd.DataFrame(data=data, columns=columns)

        if save:
            df.to_csv('processed_tweet_data.csv', index=False)
            print('File Successfully Saved.!!!')
        
        return df

                
if __name__ == "__main__":
    # required column to be generated you should be creative and add more features
#     columns = ['created_at', 'source', 'original_text','clean_text', 'sentiment','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count', 
#     'original_author', 'screen_count', 'followers_count','friends_count','possibly_sensitive', 'hashtags', 'user_mentions', 'place', 'place_coord_boundaries']
    _, tweet_list = read_json(r'C:\Users\HP\Downloads\10ACADEMY\global_twitter_data\global_twitter_data.json')
    tweet = TweetDfExtractor(tweet_list)
    tweet_df = tweet.get_tweet_df() 

# #     # use all defined functions to generate a dataframe with the specified columns above