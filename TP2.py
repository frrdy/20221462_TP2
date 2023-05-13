import requests
import os

def get_weather(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    api_key = os.environ.get("API_KEY")
    lat = os.environ.get("LAT")
    lon = os.environ.get("LON")

    data = get_weather(lat, lon, api_key)
    print(data)