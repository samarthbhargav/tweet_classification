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
#setting up the keys

class TwitterHelper(object):
    __auth = None
    __api = None
    @classmethod
    def get_auth(cls):

        if cls.__auth is None:
            twitter_conf = TwitterConfig()
            cls.__auth = OAuthHandler(twitter_conf.consumer_key, twitter_conf.consumer_secret)
            cls.__auth.set_access_token(twitter_conf.access_token, twitter_conf.access_secret)
        return cls.__auth

    @classmethod
    def get_api(cls):
        if cls.__api is None:
            cls.__api = tweepy.API(TwitterHelper.get_auth())
        return cls.__api

    @classmethod
    def get_stream(cls, limit):
        api = cls.get_api()
        auth = cls.get_auth()
        stream = tweepy.Stream(auth, TweetListener(api, limit))
        return stream


class TweetListener(StreamListener):

    def __init__(self, api, limit=100):
        self.api = api
        super(StreamListener, self).__init__()
        self._tweets = []
        self._limit = limit

    def on_data(self, data):
        js = json.loads(data, encoding="utf-8")
        if 'text' in js.keys():
            self._tweets.append(js['text'].encode('ascii', 'ignore'))
        else:
            return True
        if len(self._tweets) < self._limit:
            return True
        else:
            return False

    def on_error(self, status):
        print status
        exit(-1)

    @property
    def num_tweets(self):
        return len(self._tweets)

    @property
    def tweets(self):
        return self._tweets

if __name__ == "__main__":
    pass
