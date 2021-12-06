import tweepy

def connect_api():
    api_key = '5Tiqs5xqjVP5TrzmMRPzEjPiK'
    api_key_secret = 'WQ8m5r9KXmTWFWfZD4snLwHk8dv7EJPKrkcrwYMGG1MIBeabEu'
    beared_token = 'AAAAAAAAAAAAAAAAAAAAALlQWgEAAAAAEuUTsuCRCYOSRNGDhKoRsUuoYHI%3DBzm3qjMSQ3hTbgBTegav1Ycode91z3qJ4J9WJW3wIJ55mE3Pnp'
    access_token = '1096720487831326720-nat7ojJTrUO0xGN5RSlOnBxxhJYPDq'
    access_token_secret = 'DbygqE1F1tue8uSl6NWMMrxSkdZvMAHydDkX5qLeMBIYY'

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api


def get_tweets(api, username):
    tweets = api.user_timeline(screen_name = username)
    return print(tweets)

def search_30(api, label, query, maxResults):
    tweets = api.search_30_day(label=label, query=query, maxResults=maxResults)
    return print(tweets)


# get_tweets(connect_api(), username = 'DA39724146')
# search_30(connect_api(), label='dev', query='#parisite', maxResults=10)