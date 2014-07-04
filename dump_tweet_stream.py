
if __name__ == "__main__":
    import sys
    from twitter_api import TwitterHelper
    from processor import TweetCleaner
    import time
    
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
        streams[cl] = TwitterHelper.get_stream(limit)
        streams[cl].filter(track=cl)
        while streams[cl].listener.num_tweets < limit:
            time.sleep(1)
        print "Got tweets for class",cl,"\nWriting tweets to file"
        with open(cl+'.csv', 'w') as write:
            tweets = streams[cl].listener.tweets
            for tweet in tweets: # todo preprocessing
                tweet = TweetCleaner.process(tweet)
                write.write('{},\"{}\"\n'.format(cl, tweet))
        print "Writing to file complete"



