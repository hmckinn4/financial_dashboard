import requests

# Hardcode the Alpha Vantage API key for now
ALPHA_VANTAGE_API_KEY = 'your_alpha_vantage_api_key'

def fetch_historical_data(ticker, interval="5min"):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

def fetch_earnings_data(ticker):
    url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

def fetch_option_data(ticker):
    url = f'https://www.alphavantage.co/query?function=OPTIONS&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    print(fetch_option_data("AAPL"))
