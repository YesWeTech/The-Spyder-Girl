#! /usr/bin/env python
from os import environ # To get the environment variables
import tweepy # Manage Twitter API


# Use your Twitter API keys to connect 
auth = tweepy.OAuthHandler(environ["GIRL_KEY"], environ["GIRL_SECRET"])
auth.set_access_token(environ["GIRL_ACCESS_TOKEN"], environ["GIRL_ACCESS_SECRET"])

api = tweepy.API(auth_handler=auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
