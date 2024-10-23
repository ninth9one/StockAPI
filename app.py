# importing libraries Flask, request, jsonify
from flask import Flask, request, jsonify
import requests
import numpy as np
# !Flask! being the main class for creating the application,
# !request! will handle incoming request data (POST requests which is an HTTP method to communicate with the server main use is sending the data to the API for storage or processing)
# !jsonify! converts python dictionaries or list to JSON format for API responses
# !requests! Python library used to send HTTP requests to external APIs and retrieve responses
# reference line 2 the line imports necessary components from the Flask framework
# reference line 3 imports the requests library allowing me to make an HTTP request (calls Alpha Vantage API which will fetch stock data)
# reference line 4 imports NumPy a powerful library for numerical operations. used to calculate averages and perform numerical computations

#initialize Flask application
app = Flask(__name__)
# reference line 11 creates an instance of the Flask class by passing the special "__name__" variable which Flask uses to know where to look for the app's resources

#define API key for Alpha Vantage
ALPHA_VANTAGE_API_KEY = 'ATPXTXV4CCCUOMDP'
#stores the API key for Alpha Vantage, Alpha Vantage is a service that provides real-time stock market data. The key is used for authentication request for the Alpha Vantage API

#define a function to fetch stock data
def fetch_stock_data(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Unable to fetch stock data, lock in fr'}
# the function will be responsible for making request to 'Alpha vantage API' to get stock data
# !ticker! a parameter that represents the stock ticker symbol (e.g. AAPL for Apple)
# !url! API endpoint with the required query parameters (e.g. ticker symbol, time interval, API key)
# !requests.get(url)! sends an HTTP GET (another HTTP method to communicate with the server) comparison GET is for retrieving data without modifying it POST is for sending data that often causes changes or requires more secure transmission
# !response.status_code == 200! checks if the request was successful (status code 200 shows that its a success)
# !response.json()! converts the response from JSON format to a Python dictionary
# line 28 an error message using !return!

# create an API route to get stock data
@app.route('/api/stock/<ticker>', methods=['GET'])
def get_stock(ticker):
    data = fetch_stock_data(ticker)
    return jsonify(data)
# !@app.route('/api/stock/<ticker>', methods=['GET'])! defines an API route that listens for GET requests the
# !ticker! part is a URL parameter that allows the client to pass the stock ticker dynamically
# !get_stock(ticker)! function handles the request calling fetch_stock_data() to retrieve the stock data and return it as a JSON response using !jsonify()!

# simulate trend anaylsis
def trend_analysis(ticker):
    # Placeholder data for demonstration
    return {
        'ticker': ticker,
        'moving_average': 50,
        'rsi': 14,
        'recommendation': 'buy' if ticker.lower() == 'aapl' else 'hold'
    }
# !moving_average! A simple moving average
# !rsi! Relative strength Index
# !recommendation! A simplistic recommendation based on whether the stock is Apple (AAPL)

# create an API route for Trend Analysis
@app.route('/api/trend_analysis/<ticker>', methods=['GET'])
def get_trend_analysis(ticker):
    data = trend_analysis(ticker)
    return jsonify(data)
# defines another API route that provides trend analysis for the specified stock ticker
# !trend_analysis()! function is used to return the placeholder analysis data as a JSON response

# simulating a trade
@app.route('/api/trade', methods=['POST'])
def place_trade():
    trade_data = request.json
    ticker = trade_data.get('ticker')
    action = trade_data.get('action')
    quantity = trade_data.get('quantity')
    price = trade_data.get('price')

    # Example logic for placing a trade
    if action.lower() not in ['buy', 'sell']:
        return jsonify({'message': 'Invalid action. Must be "buy" or "sell".'}), 400

    return jsonify({
        'message': f'{action.capitalize()} order placed for {quantity} shares of {ticker} at ${price} per share.'
    })
# this route listens to POST requests at !/api/trade! simulates stock trades
# !request.json! retrieves the JSON data sent in the request body
# the code extracts the !ticker! !action! !quantity! !price! from the request data
# the trade is validated to ensure the action is either !buy! or !sell! if not it returns a 400 error with a message
# if valid it will return a confirmation message

# run the flask app
if __name__ == '__main__':
    app.run(debug=True)
# this is the entry point of the application, when the script is executed the flask server starts up
# !debug=True! this enables flask's debug mode, which provides error messages during development
