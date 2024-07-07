from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Example function to generate signals based on a simple logic
def generate_signals(symbol):
    # Example candlestick data with time in minutes
    candlestick_data = {
        "FX:EURUSD": [
            {"time": 1, "high": 1.1000, "low": 1.0950},
            {"time": 2, "high": 1.1010, "low": 1.0960},
            {"time": 3, "high": 1.1020, "low": 1.0970},
            {"time": 4, "high": 1.1030, "low": 1.0940},
            {"time": 5, "high": 1.1040, "low": 1.0980}
        ],
        "FX:GBPUSD": [
            {"time": 1, "high": 1.2500, "low": 1.2450},
            {"time": 2, "high": 1.2510, "low": 1.2460},
            {"time": 3, "high": 1.2520, "low": 1.2470},
            {"time": 4, "high": 1.2530, "low": 1.2440},
            {"time": 5, "high": 1.2540, "low": 1.2480}
        ],
        "FX:USDJPY": [
            {"time": 1, "high": 110.50, "low": 110.00},
            {"time": 2, "high": 110.60, "low": 110.10},
            {"time": 3, "high": 110.70, "low": 110.20},
            {"time": 4, "high": 110.80, "low": 110.30},
            {"time": 5, "high": 110.90, "low": 110.40}
        ],
        "FX:AUDUSD": [
            {"time": 1, "high": 0.7500, "low": 0.7450},
            {"time": 2, "high": 0.7510, "low": 0.7460},
            {"time": 3, "high": 0.7520, "low": 0.7470},
            {"time": 4, "high": 0.7530, "low": 0.7440},
            {"time": 5, "high": 0.7540, "low": 0.7480}
        ],
        "FX:USDCAD": [
            {"time": 1, "high": 1.3500, "low": 1.3450},
            {"time": 2, "high": 1.3510, "low": 1.3460},
            {"time": 3, "high": 1.3520, "low": 1.3470},
            {"time": 4, "high": 1.3530, "low": 1.3440},
            {"time": 5, "high": 1.3540, "low": 1.3480}
        ],
        "FX:USDCHF": [
            {"time": 1, "high": 0.9900, "low": 0.9850},
            {"time": 2, "high": 0.9910, "low": 0.9860},
            {"time": 3, "high": 0.9920, "low": 0.9870},
            {"time": 4, "high": 0.9930, "low": 0.9840},
            {"time": 5, "high": 0.9940, "low": 0.9880}
        ],
        "FX:NZDUSD": [
            {"time": 1, "high": 0.7100, "low": 0.7050},
            {"time": 2, "high": 0.7110, "low": 0.7060},
            {"time": 3, "high": 0.7120, "low": 0.7070},
            {"time": 4, "high": 0.7130, "low": 0.7040},
            {"time": 5, "high": 0.7140, "low": 0.7080}
        ],
        # Add more data for other pairs as needed
    }

    signals = []
    data = candlestick_data.get(symbol, [])

    for i in range(1, len(data)):
        prev = data[i - 1]
        curr = data[i]

        if curr["high"] > prev["high"]:
            signals.append(f"Buy signal: Higher high detected for {symbol} at time {curr['time']} minutes")
        if curr["low"] < prev["low"]:
            signals.append(f"Sell signal: Lower low detected for {symbol} at time {curr['time']} minutes")

    for _ in range(random.randint(1, 3)):
        signals.append(random.choice([
            f"Buy signal: Random condition for {symbol} at random time",
            f"Sell signal: Random condition for {symbol} at random time"
        ]))

    return signals

@app.route('/get_signals', methods=['GET'])
def get_signals():
    symbol = request.args.get('symbol', 'FX:EURUSD')
    signals = generate_signals(symbol)
    return jsonify(signals)

if __name__ == "__main__":
    app.run(debug=True)
