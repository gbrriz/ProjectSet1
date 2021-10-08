import tweepy
import pymongo
import json
import logging
from config import TWITTER

client = pymongo.MongoClient("mongodb")
db = client.tweets
collection = db.tweet_data

### SECTION 1: GET THE CREDENTIALS

CONSUMER_KEY = TWITTER['consumer_key']
CONSUMER_SECRET = TWITTER['consumer_secret']
ACCESS_TOKEN = TWITTER['access_token']
ACCESS_TOKEN_SECRET = TWITTER['access_token_secret']

### SECTION 2: AUTHENTIFICATION TO TWITTER API 

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

#### CREATE TWITTER API OBJECT
api = tweepy.API(auth_handler=auth,
                 wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

### SOME FUNCTIONALITIES

# write a tweet: 
# update status

#api.update_status("Hello! I am sending a tweet from a code.")

### SEARCHING FOR TWITTER
# tweepy Cursor with api.search

cursor = tweepy.Cursor(api.search,
                       q = "sumac -filter:retweets",
                       lang = "en",
                       tweet_mode = "extended").items(5)

for tweet in cursor:
    collection.insert_one(tweet.fulltext)
