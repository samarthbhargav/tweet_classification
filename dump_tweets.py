
if __name__ == "__main__":
    import sys
    from twitter_api import TweetGetter
    from processor import TweetCleaner
    if len(sys.argv) < 3:
        print "Usage: {} <num_tweets_to_fetch> <class1> [<class2> [<class3> ..]]".format(sys.argv[0])
        exit(-1)

    try:
        limit = int(sys.argv[1])
    except:
        print "First Argument should be an int"
        exit(-1)
    classes = sys.argv[2:]
    streams = dict()
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



