from financial_dashboard.backend.data_fetching.yahoo_finance import fetch_historical_data, fetch_earnings_data
from financial_dashboard.backend.data_fetching.robinhood import fetch_option_data
from financial_dashboard.backend.data_fetching.twitter import twitter_api_setup, fetch_tweets
from financial_dashboard.backend.data_fetching.open_ai_api import query_openai

def main():
    # Fetch historical data
    historical_data = fetch_historical_data("AAPL", "1y")
    print("Historical Data:")
    print(historical_data)

    # Fetch earnings data
    earnings_data = fetch_earnings_data("AAPL")
    print("Earnings Data:")
    print(earnings_data)

    # Fetch option data
    option_data = fetch_option_data("AAPL")
    print("Option Data:")
    print(option_data)

    # Fetch tweets
    api = twitter_api_setup()
    tweets = fetch_tweets(api, "AAPL", 10)
    print("Tweets:")
    for tweet in tweets:
        print(tweet.text)

    # Query OpenAI
    prompt = "Tell me about the recent performance of Apple stock."
    openai_response = query_openai(prompt)
    print("OpenAI Response:")
    print(openai_response)

if __name__ == "__main__":
    main()
