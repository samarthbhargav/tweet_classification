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

class _TwitterConfig(object):
    __auth = None
    @classmethod
    def get_auth(cls):

        if cls.__auth is None:
            twitter_conf = TwitterConfig()
            cls.__auth = OAuthHandler(twitter_conf.consumer_key, twitter_conf.consumer_secret)
            cls.__auth.set_access_token(twitter_conf.access_token, twitter_conf.access_secret)
        return cls.__auth


class TweetListener(StreamListener):

    def __init__(self, *args, **kwargs):
        super(TweetListener, self).__init__(*args, **kwargs)
        self.__tweets = []

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
    #stream = Stream(auth, TweetListener())
    #print stream.filter(track=['india'])
    #api = tweepy.API(auth)
    pass
