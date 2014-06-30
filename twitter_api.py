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

    def __init__(self, api):
        self.api = api
        super(StreamListener, self).__init__()
        self._tweets = []

    def on_data(self, data):
        js = json.loads(data, encoding="utf-8")
        self._tweets.append(js['text'].encode('ascii', 'ignore'))
        return True

    def on_error(self, status):
        print status
        exit(-1)

class TweetStream(object):

    def __init__(self,auth_obj,stream_name):
        self.__stream = Stream(auth_obj, TweetListener())
        self.__stream_name = stream_name
        self.__complete = False

    def start_stream(self):
        self.__complete = False
        self.__stream.filter(track=[self.__stream_name])

    def kill(self):
        self.__complete = True
        self.__stream.disconnect()

    def get_tweets(self):
        return self.__stream._tweets

    @property
    def is_complete(self):
        return self.__complete

    @property
    def num_tweets(self):
        return len(self.__stream._tweets)

class ShortTweetStream(TweetStream):

    def get_stream_as_list(self):
        pass

if __name__ == "__main__":
    ts = TweetStream(_TwitterConfig.get_auth,'india')
    print ts.num_tweets

