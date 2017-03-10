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

import facebook
from os import environ
import requests

# connect to facebook
graph = facebook.GraphAPI(access_token=environ['FACEBOOK_ACCESS_TOKEN'], version='2.7')
# download notifications and likes from facebook.
data = graph.get_object(id="me", fields="feed{likes{id,name}},notifications{from}")

def get_feed_names():
    # create a empty dictionary
    global data
    data_feed = data['feed']
    names = {}

    while(True):
        try:
            # iterate the feed posts
            for feed in data_feed['data']:
                # iterate over likes on each post
                if 'likes' in feed:
                    for like in feed['likes']['data']:
                        if like['name'] not in names:
                            names[like['name']] = 1
                        else:
                            names[like['name']] += 1
            data_feed = requests.get(data_feed['paging']['next']).json()
        except KeyError:
            break

    return names
