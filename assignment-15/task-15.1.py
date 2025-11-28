import requests

def fetch_city_weather(city_name: str, api_key: str) -> dict:
    """
    Fetch weather details for a given city using the OpenWeatherMap API.

    Args:
        city_name: Name of the city to fetch the weather for.
        api_key: API key for authenticating with the weather service.

    Returns:
        JSON response payload as a Python dictionary.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
    }

    response = requests.get(base_url, params=params, timeout=10)
    weather_data = response.json()
    print(weather_data)
    return weather_data

def test_fetch_city_weather():
    """Test cases for fetch_city_weather function."""
    api_key = "ff6aa4c18255076bae9b5ee8fb0048d8"
    
    # Test case 1: Valid city name should return a dictionary with expected keys
    print("Test 1: Valid city name")
    weather_data = fetch_city_weather("warangal", api_key)
    assert isinstance(weather_data, dict), "Weather data should be a dictionary"
    assert "name" in weather_data, "Response should contain 'name' key"
    assert "main" in weather_data, "Response should contain 'main' key"
    assert "weather" in weather_data, "Response should contain 'weather' key"
    print("✓ Test 1 passed")
    
    # Test case 2: Response should contain temperature data
    print("\nTest 2: Temperature data in response")
    weather_data = fetch_city_weather("london", api_key)
    assert "main" in weather_data, "Response should contain 'main' key"
    assert "temp" in weather_data["main"], "Main should contain 'temp' key"
    assert isinstance(weather_data["main"]["temp"], (int, float)), "Temperature should be a number"
    print("✓ Test 2 passed")
    
    # Test case 3: Response should contain weather description
    print("\nTest 3: Weather description in response")
    weather_data = fetch_city_weather("mumbai", api_key)
    assert "weather" in weather_data, "Response should contain 'weather' key"
    assert len(weather_data["weather"]) > 0, "Weather array should not be empty"
    assert "description" in weather_data["weather"][0], "Weather should contain 'description'"
    print("✓ Test 3 passed")
    
    print("\n✅ All test cases passed!")


if __name__ == "__main__":
    city_name = "warangal"
    api_key = "ff6aa4c18255076bae9b5ee8fb0048d8"
    weather_data = fetch_city_weather(city_name, api_key)
    print(weather_data)
    
    # Run test cases
    print("\n" + "="*50)
    print("Running test cases...")
    print("="*50)
    test_fetch_city_weather()