import tweepy

# Use your own credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

def twitter_api_setup():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

def fetch_tweets(api, query, count=100):
    tweets = api.search(q=query, count=count)
    return tweets

if __name__ == "__main__":
    api = twitter_api_setup()
    tweets = fetch_tweets(api, "AAPL", 10)
    for tweet in tweets:
        print(tweet.text)
