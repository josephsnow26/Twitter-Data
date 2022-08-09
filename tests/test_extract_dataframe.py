# Skip to content
# Search or jump to…
# Pull requests
# Issues
# Marketplace
# Explore
 
# @josephsnow26 
# josephsnow26
# /
# Twitter-Data
# Public
# generated from 10xac/Twitter-Data-Analysis-Template
# Code
# Issues
# Pull requests
# Actions
# Projects
# Wiki
# Security
# Insights
# Settings
# Twitter-Data/tests/test_extract_dataframe.py /
# @josephsnow26
# josephsnow26 Initial commit
# Latest commit 36a414e 17 hours ago
#  History
#  1 contributor
# 100 lines (76 sloc)  2.81 KB

import unittest
import pandas as pd
import sys, os

sys.path.append(os.path.abspath(os.path.join("../..")))

from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor

# For unit testing the data reading and processing codes, 
# we will need about 5 tweet samples. 
# Create a sample not more than 10 tweets and place it in a json file.
# Provide the path to the samples tweets file you created below
sampletweetsjsonfile = "./system.json"   #put here the path to where you placed the file e.g. ./sampletweets.json. 
# _, tweet_list = read_json(r'C:\Users\HP\Downloads\10ACADEMY\global_twitter_data\global_twitter_data.json')

# columns = [
# #     "created_at",
# #     "source",
# #     "full_text",
#     "clean_text",
#     "sentiment",
#     "polarity",
#     "subjectivity",
# #     "lang",
# #     "favorite_count",
# #     "retweet_count",
#     "original_author",
#     "screen_count",
# #     "followers_count",
# #     "friends_count",
#     "possibly_sensitive",
#     "hashtags",
#     "user_mentions",
#     "place",
#     "place_coord_boundaries",
# ]


class TestTweetDfExtractor(unittest.TestCase):
    """
		A class for unit-testing function in the fix_clean_tweets_dataframe.py file
		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.df = TweetDfExtractor(tweet_list[:5])
        tweet_df = self.df.get_tweet_df()
        

    def test_find_statuses_count(self):
        self.assertEqual(self.df.find_statuses_count(),[8097,5831,1627,1627,18958])
        
        
    def test_find_followers_count(self):
        f_count = [20497,65,85,85,910]
        self.assertEqual(self.df.find_followers_count(), f_count)

    def test_find_friends_count(self):
        friends_count = [2621,272,392,392,2608]
        self.assertEqual(self.df.find_friends_count(), friends_count)

#     def test_find_full_text(self):
#         text = <provide a list of the first five full texts>

#         self.assertEqual(self.df.find_full_text(), text)

#     def test_find_sentiments(self):
#         self.assertEqual(
#             self.df.find_sentiments(self.df.find_full_text()),
#             (
#                 <provide a list of the first five sentiment values>,
#                 <provide a list of the first five polarity values>,
#             ),
#         )


#     def test_find_screen_name(self):
#         name = <provide a list of the first five screen names>
#         self.assertEqual(self.df.find_screen_name(), name)

    

#     def test_find_is_sensitive(self):
#         self.assertEqual(self.df.is_sensitive(), <provide a list of the first five is_sensitive values>)


#     # def test_find_hashtags(self):
    #     self.assertEqual(self.df.find_hashtags(), )

    # def test_find_mentions(self):
    #     self.assertEqual(self.df.find_mentions(), )



if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


