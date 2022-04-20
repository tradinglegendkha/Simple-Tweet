import tweepy
import pandas as pd
import config as con

auth = tweepy.OAuthHandler(con.consumer_key, con.consumer_secret)
auth.set_access_token(con.access_token, con.access_token_secret)
api = tweepy.API(auth)

number_of_tweets = 10
tweets = []
likes = []
time = []

for i in tweepy.Cursor(api.user_timeline, id="DeItaone", tweet_mode="extended").items(number_of_tweets):
    tweets.append(i.full_text)
    likes.append(i.favorite_count)
    time.append(i.created_at)

df = pd.DataFrame({"tweets":tweets, "likes":likes, "time":time})

print(df)


