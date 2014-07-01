
if __name__ == "__main__":
    import sys
    from twitter_api import TwitterHelper
    from processor import TweetCleaner
    import time
    classes = sys.argv[1:]
    streams = dict()
    limit = 100
    print "Classes: ", classes, "  Number of Tweets to fetch : " , limit
    for cl in classes:
        print "Getting Tweets for class", cl
        streams[cl] = TwitterHelper.get_stream(limit)
        streams[cl].filter(track=cl)
        while streams[cl].listener.num_tweets < limit:
            time.sleep(1)
        print "Got tweets for class",cl,"\nWriting tweets to file"
        with open(cl+'.csv', 'w') as write:
            tweets = streams[cl].listener.tweets
            for tweet in tweets: # todo preprocessing
                tweet = TweetCleaner.strip_special_chars(tweet)
                write.write('{},\"{}\"\n'.format(cl, tweet))
        print "Writing to file complete"



