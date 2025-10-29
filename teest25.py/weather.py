import requests
import json
import os
import time

API_KEY = "YOUR_METEOSOURCE_API_KEY"
BASE_URL = "https://www.meteosource.com/api/v1/free/point"
CACHE_FILE = "weather_cache.json"
CACHE_EXPIRY = 3600

def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_cache(cache):
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f)
    except:
        pass

def get_weather_from_api(city):
    params = {
        "place_id": city,
        "sections": "current",
        "units": "metric",
        "language": "uk",
        "key": API_KEY
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        current = data.get("current", {})
        return {
            "city": city,
            "temperature": current.get("temperature"),
            "conditions": current.get("summary")
        }
    except:
        return None

def get_weather(city="kyiv"):
    cache = load_cache()
    now = time.time()
    if city in cache:
        entry = cache[city]
        if now - entry["timestamp"] < CACHE_EXPIRY:
            return entry["data"]
    weather_data = get_weather_from_api(city)
    if weather_data:
        cache[city] = {"timestamp": now, "data": weather_data}
        save_cache(cache)
    return weather_data

def main():
    weather_info = get_weather("kyiv")
    if weather_info:
        print("City:", weather_info["city"])
        print("Temperature:", weather_info["temperature"], "°C")
        print("Conditions:", weather_info["conditions"])
    else:
        print("Failed to get weather data")

if __name__ == "__main__":
    main()
