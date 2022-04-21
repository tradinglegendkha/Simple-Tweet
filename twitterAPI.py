import tweepy
import pandas as pd
import config as con

auth = tweepy.OAuthHandler(con.consumer_key, con.consumer_secret)
auth.set_access_token(con.access_token, con.access_token_secret)
api = tweepy.API(auth)

number_of_tweets = 10 #numbmer of tweets  
time = []
tweets = []
#likes = []

def tweets(): 
    for i in tweepy.Cursor(api.user_timeline, id="DeItaone", tweet_mode="extended").items(number_of_tweets):
        try: #twitter has rate limit, so theres no way to fix the incomplete tweets
            tweets.append(i.retweeted_status.full_text)
        except AttributeError:
            print(i.full_text)
        #likes.append(i.favorite_count)
        #time.append(i.created_at)

#df = pd.DataFrame({"time":time, "tweets":tweets}) #data frame, how the tweets are displayed
#print(df)
