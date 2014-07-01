
if __name__ == "__main__":

    from twitter_api import TwitterHelper
    import time
    classes = ['basketball', 'cricket', 'football']
    streams = dict()
    limit = 100
    for cl in classes:
        streams[cl] = TwitterHelper.get_stream(limit)
        streams[cl].filter(track=cl)
        while streams[cl].listener.num_tweets < limit:
            time.sleep(1)
        with open(cl+'.csv', 'w') as write:
            tweets = streams[cl].listener.tweets
            for tweet in tweets: # todo cleaning
                write.write('{},\"{}\"\n'.format(cl, tweet))



