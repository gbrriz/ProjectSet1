import json
import logging
import tweepy
import pymongo
from config import TWITTER

client = pymongo.MongoClient('mongodb')
db = client.tweets
collection = db.tweet_data
### Section 1 ###

### get credentials ###

CONSUMER_KEY = TWITTER['consumer_key']
CONSUMER_SECRET = TWITTER['consumer_secret']
ACCESS_TOKEN = TWITTER['access_token']
ACCESS_TOKEN_SECRET = TWITTER['access_token_secret']


#logging.basicConfig(filename="logfile.log",
#filemode='w')

### SECTION 2 ###

### authenticate to Twitter

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)


### SECTION 3 STREAMING 


#override tweepy.StreamListener to add logic to on_status
class MaxTweetsListener(tweepy.StreamListener):
    
    
    def __init__(self, max_tweets, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_tweets = max_tweets
        self.counter = 0
    
    def on_connect(self):
        logging.critical('CONNECTED')

    def on_data(self, data):
        """Whatever we put in this method defines what is done with
        every single tweet as it is intercepted in real-time"""
        
        t = json.loads(data) # t is just a regular python dictionary.
        
        tweet = {'text': t['text'],
            'username': t['user']['screen_name'],
            'followers_count': t['user']['followers_count']
        }
        logging.critical(f' TWEET INCOMING: \n\n\n{tweet["username"]}:{tweet["text"]}\n\n\n')
        # 
        collection.insert_one(tweet)
        logging.critical('TWEET INSERTED')
        
        self.counter += 1
        if self.max_tweets == self.counter:
            self.counter=0
            return False
        
    def on_error(self, status_code):
        if status_code == 400:
             logging.error('rate limited')
        if status_code == 420:
            logging.error('rate limited')
            #returning False in on_error disconnects the stream
            return False

if __name__ == '__main__':

    # create a listener object
    max_tweets_listener = MaxTweetsListener(max_tweets=5)
    # setup the stream
    stream = tweepy.Stream(auth=auth, listener=max_tweets_listener) 
    # filter the stream
    stream.filter(track=['sumac'],languages=['en'])