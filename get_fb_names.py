import facebook
from os import environ

# connect to facebook
graph = facebook.GraphAPI(access_token=environ['FACEBOOK_ACCESS_TOKEN'], version='2.7')
# download notifications and likes from facebook.
data = graph.get_object(id="me", fields="feed{likes{id,name}},notifications{from}")

def get_feed_names():
    # create a empty dictionary
    names = {}

    # iterate the feed posts
    for feed in data['feed']['data']:
        # iterate over likes on each post
        if 'likes' in feed:
            for like in feed['likes']['data']:
                if like['name'] not in names:
                    names[like['name']] = 1
                else:
                    names[like['name']] += 1

    return names
