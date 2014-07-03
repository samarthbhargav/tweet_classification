tweet_classification (WIP)
====================
An Attempt to perform simple classification on Tweets that is fetched from a tweet stream. 

Uses sklearn for the classification and tweepy for the Twitter api.

Running the code
----------------------
For running this code, you need to have a twitter dev account. After creating the account
you need to clone this repo and make a directory in the same folder named _config.py 
In this file, please enter the follwowing 
```
_config = {
‘consumer_key’ :’’, # your consumer_key
‘consumer_secret’ : ‘’, # your consumer_secret
‘access_token’ : ‘’, # your access_token
‘access_secret’ : ‘’ # your access_secret
}
```

That’s it! 

To create training data, run the dump_tweets.py with the stream names as arguments. So for example if you need 
to get streams of ‘basketball’ and ‘football’, you type:

`python dump_tweets.py basketball football`

Citations
----------------------------
I referred the following sources 

- tweepy : http://sachithdhanushka.blogspot.in/2014/02/mining-twitter-data-using-python.html
