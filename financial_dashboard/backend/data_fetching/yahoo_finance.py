import yfinance as yf

def fetch_historical_data(ticker, period="1y"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    return hist

def fetch_earnings_data(ticker):
    stock = yf.Ticker(ticker)
    earnings = stock.earnings
    return earnings

if __name__ == "__main__":
    print(fetch_historical_data("AAPL", "1y"))
    print(fetch_earnings_data("AAPL"))
