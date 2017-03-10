import tweepy # Manage Twitter API
from os import environ # To get the environment variables

# Use your Twitter API keys to connect 

auth = tweepy.OAuthHandler(environ["TWITTER_CONSUMER_KEY"], 
                           environ["TWITTER_CONSUMER_SECRET"])

auth.set_access_token(environ["TWITTER_ACCESS_TOKEN"], 
                      environ["TWITTER_ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth_handler=auth, wait_on_rate_limit_notify=True, 
wait_on_rate_limit=True)

