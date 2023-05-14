import os
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def get_weather(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/weather', methods=['GET'])
def weather():
    api_key = os.environ.get("API_KEY")

    lat = request.args.get("lat")
    lon = request.args.get("lon")
    result = get_weather(lat, lon, api_key)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8081)