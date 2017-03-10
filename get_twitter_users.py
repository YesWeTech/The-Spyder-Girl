import tweepy  # Manage Twitter API
import pandas as pd  # to create dataframes
from os import environ  # To get the environment variables

# Use your Twitter API keys to connect

auth = tweepy.OAuthHandler(environ["TWITTER_CONSUMER_KEY"],
                           environ["TWITTER_CONSUMER_SECRET"])

auth.set_access_token(environ["TWITTER_ACCESS_TOKEN"],
                      environ["TWITTER_ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth_handler=auth, wait_on_rate_limit_notify=True,
                 wait_on_rate_limit=True)


def get_time_line_retweeters():

    tweets_list = []
    # get the tweets of our timeline
    timeline = api.user_timeline(
        by_screenname='geekantechgirl', count=200, include_rts=False)
    # construct the dataframe
    for tweet in timeline:

        tweets_list.append([str(tweet.id), int(tweet._json['favorite_count']),
                            str(tweet._json['retweet_count']), tweet.created_at])

    tweets = pd.DataFrame(data=tweets_list,
                          columns=['id', 'like', 'retweet', 'date'])

    return tweets


print(get_time_line_retweeters())
