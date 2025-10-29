import unittest
import weather
import os
import time

class TestWeather(unittest.TestCase):

    def setUp(self):
        if os.path.exists(weather.CACHE_FILE):
            os.remove(weather.CACHE_FILE)

    def test_load_empty_cache(self):
        cache = weather.load_cache()
        self.assertEqual(cache, {})

    def test_save_and_load_cache(self):
        data = {"kyiv": {"timestamp": time.time(), "data": {"temperature": 20, "conditions": "sunny"}}}
        weather.save_cache(data)
        loaded = weather.load_cache()
        self.assertEqual(loaded["kyiv"]["data"]["temperature"], 20)

    def test_get_weather_from_api_success(self):
        result = weather.get_weather_from_api("kyiv")
        self.assertIsInstance(result, dict)
        self.assertIn("temperature", result)
        self.assertIn("conditions", result)

    def test_get_weather_from_api_fail(self):
        result = weather.get_weather_from_api("invalid_city_123")
        self.assertTrue(result is None or isinstance(result, dict))

    def test_get_weather_cache_hit(self):
        city = "kyiv"
        data = {"timestamp": time.time(), "data": {"temperature": 25, "conditions": "sunny"}}
        weather.save_cache({city: data})
        result = weather.get_weather(city)
        self.assertEqual(result["temperature"], 25)

    def test_get_weather_cache_expired(self):
        city = "kyiv"
        old_time = time.time() - (weather.CACHE_EXPIRY + 10)
        data = {"timestamp": old_time, "data": {"temperature": 25, "conditions": "sunny"}}
        weather.save_cache({city: data})
        result = weather.get_weather(city)
        self.assertIsInstance(result, dict)

    def test_get_weather_invalid_city(self):
        result = weather.get_weather("invalid_city_123")
        self.assertTrue(result is None or isinstance(result, dict))

    def test_cache_file_created(self):
        city = "kyiv"
        weather.get_weather(city)
        self.assertTrue(os.path.exists(weather.CACHE_FILE))

if __name__ == "__main__":
    unittest.main()