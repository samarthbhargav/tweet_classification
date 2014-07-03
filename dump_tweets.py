
if __name__ == "__main__":
    import sys
    from twitter_api import TweetGetter
    from processor import TweetCleaner
    classes = sys.argv[1:]
    streams = dict()
    limit = 100
    print "Classes: ", classes, "  Number of Tweets to fetch : " , limit
    for cl in classes:
        print "Getting Tweets for class", cl
        streams[cl] = TweetGetter.get_n_tweets_by_user(cl, limit)
        print "Got tweets for class",cl,"\nWriting tweets to file"
        with open(cl+'.csv', 'w') as write:
            tweets = streams[cl]
            for tweet in tweets: # todo preprocessing
                tweet = TweetCleaner.process(tweet)
                write.write('{},\"{}\"\n'.format(cl, tweet))
        print "Writing to file complete"



