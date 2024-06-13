from flask import Flask, jsonify, request
from financial_dashboard.backend.data_fetching.yahoo_finance import fetch_historical_data, fetch_earnings_data, fetch_option_data
from financial_dashboard.backend.data_fetching.twitter import twitter_api_setup, fetch_tweets
from financial_dashboard.backend.data_fetching.open_ai_api import query_openai

app = Flask(__name__)

@app.route('/historical_data/<string:ticker>', methods=['GET'])
def get_historical_data(ticker):
    interval = request.args.get('interval', '5min')
    data = fetch_historical_data(ticker, interval)
    return jsonify(data)

@app.route('/earnings_data/<string:ticker>', methods=['GET'])
def get_earnings_data(ticker):
    data = fetch_earnings_data(ticker)
    return jsonify(data)

@app.route('/option_data/<string:ticker>', methods=['GET'])
def get_option_data(ticker):
    data = fetch_option_data(ticker)
    return jsonify(data)

@app.route('/tweets/<string:ticker>', methods=['GET'])
def get_tweets(ticker):
    count = int(request.args.get('count', 10))
    api = twitter_api_setup()
    tweets = fetch_tweets(api, ticker, count)
    return jsonify([tweet.text for tweet in tweets])

@app.route('/openai', methods=['POST'])
def openai_query():
    prompt = request.json.get('prompt')
    response = query_openai(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
