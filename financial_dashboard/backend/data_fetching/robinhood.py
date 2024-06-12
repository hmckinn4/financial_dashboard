import robin_stocks.robinhood as r

# Use your own credentials
USERNAME = 'your_username'
PASSWORD = 'your_password'

r.login(USERNAME, PASSWORD)

def fetch_option_data(ticker):
    options = r.options.get_available_options(ticker)
    return options

if __name__ == "__main__":
    print(fetch_option_data("AAPL"))
