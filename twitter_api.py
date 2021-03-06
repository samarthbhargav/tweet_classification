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

# source : https://gist.github.com/yanofsky/5436496
class TweetGetter(object):

    @staticmethod
    def get_n_tweets_by_user(screen_name, n):

        def conv_to_text_vec(status_list):
            return [status.text.encode('ascii','ignore') for status in status_list]

        alltweets = []
        max_tweets = 200 # this is the API limit
        api = TwitterHelper.get_api()

        if n < max_tweets:
            return conv_to_text_vec(api.user_timeline(screen_name = screen_name,count=n))

        new_tweets = api.user_timeline(screen_name = screen_name,count=max_tweets)

        alltweets.extend( new_tweets )
        oldest = alltweets[-1].id - 1

        while len(new_tweets) > 0:
            new_tweets = api.user_timeline(screen_name = screen_name, count = max_tweets, max_id = oldest)
            alltweets.extend(new_tweets)

            if len(alltweets) > n:
                return conv_to_text_vec(alltweets)[:n]

            oldest = alltweets[-1].id - 1


if __name__ == "__main__":

    # tests for Tweetgetter
    screen_name = 'nba'
    tweets = TweetGetter.get_n_tweets_by_user(screen_name, 1000)

    print "Got {} tweets from user {}:\n{}".format(len(tweets), screen_name, "\n".join(tweets))
    print "\n\n", len(tweets)
