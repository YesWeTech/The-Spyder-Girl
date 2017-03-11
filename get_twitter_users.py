"""
This file is part of The-Spyder-Girl.

    The-Spyder-Girl is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    The-Spyder-Girl is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with The-Spyder-Girl.  If not, see <http://www.gnu.org/licenses/>.
"""

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


def get_timeline_data():

    tweets_list = []
    # construct the dataframe
    for tweet in tweepy.Cursor(api.user_timeline, include_rts=False).items():

        tweets_list.append([str(tweet.id), int(tweet._json['favorite_count']),
                            str(tweet._json['retweet_count']), tweet.created_at])

    tweets = pd.DataFrame(data=tweets_list,
                          columns=['id', 'like', 'retweet', 'date'])

    return tweets

data = get_timeline_data()
data.to_csv("twiter.csv", sep='\t')
print(data)
