# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 18:09:48 2014

@author: hduser
"""

# SOURCE http://sachithdhanushka.blogspot.in/2014/02/mining-twitter-data-using-python.html

#imports
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
from config import TwitterConfig
import json
import time
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

    def __init__(self, api, limit=100):
        self.api = api
        super(StreamListener, self).__init__()
        self._tweets = []
        self._limit = limit

    def on_data(self, data):
        js = json.loads(data, encoding="utf-8")
        self._tweets.append(js['text'].encode('ascii', 'ignore'))
        if len(self._tweets) < self._limit:
            return True
        else:
            return False

    def on_error(self, status):
        print status
        exit(-1)



if __name__ == "__main__":
    auth = _TwitterConfig.get_auth()
    api = tweepy.API(auth)
    stream = tweepy.Stream(auth, TweetListener(api, 10))

    stream.filter(track=['india'])
