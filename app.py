from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Welcome to Weather API',
        'version': '1.0',
        'status': 'active'
    })


@app.route('/weather')
def weather():
    """Weather endpoint"""
    return jsonify({
        'location': 'New York',
        'temperature': 72,
        'unit': 'Fahrenheit',
        'condition': 'Partly Cloudy',
        'humidity': 65,
        'wind_speed': 12
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)