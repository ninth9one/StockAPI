from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Alpha Vantage API Key
ALPHA_VANTAGE_API_KEY = 'OY4JYLS1L3V5SR8O'

# Fetch real-time stock data from Alpha Vantage API
def fetch_stock_data(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Unable to fetch stock data'}

# API route to get stock data
@app.route('/api/stock/<ticker>', methods=['GET'])
def get_stock(ticker):
    data = fetch_stock_data(ticker)
    return jsonify(data)

# Simulate trend analysis (this is a placeholder for actual analysis logic)
def trend_analysis(ticker):
    # Placeholder data for demonstration
    return {
        'ticker': ticker,
        'moving_average': 50,
        'rsi': 14,
        'recommendation': 'buy' if ticker.lower() == 'aapl' else 'hold'
    }

# API route for trend analysis
@app.route('/api/trend_analysis/<ticker>', methods=['GET'])
def get_trend_analysis(ticker):
    data = trend_analysis(ticker)
    return jsonify(data)

# Simulate trade (this is a placeholder for actual trade logic)
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

    # Simulate success response
    return jsonify({
        'message': f'{action.capitalize()} order placed for {quantity} shares of {ticker} at ${price} per share.'
    })

if __name__ == '__main__':
    app.run(debug=True)
