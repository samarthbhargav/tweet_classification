# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 18:09:48 2014

@author: hduser
"""

# SOURCE http://sachithdhanushka.blogspot.in/2014/02/mining-twitter-data-using-python.html

#imports
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#import tweepy
from config import TwitterConfig
import json
#setting up the keys
twitter_conf = TwitterConfig()
class TweetListener(StreamListener):
    # A listener handles tweets are the received from the stream.
    #This is a basic listener that just prints received tweets to standard output

    def on_data(self, data):
        js = json.loads(data, encoding="utf-8")
        print js['text'].encode('ascii', 'ignore')
        return True

    def on_error(self, status):
        print status


class TweetStream(object):

    def __init__(self, stream):
        self.__stream = stream


    def kill(self):
        pass

    def get_tweets(self):
        pass


class ShortTweetStream(TweetStream):

    def get_stream_as_list(self):
        pass

if __name__ == "__main__":
    auth = OAuthHandler(twitter_conf.consumer_key, twitter_conf.consumer_secret)
    auth.set_access_token(twitter_conf.access_token, twitter_conf.access_secret)

    stream = Stream(auth, TweetListener())
    print stream.filter(track=['india'])
    #api = tweepy.API(auth)
