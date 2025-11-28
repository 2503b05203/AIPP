import requests
import json
import sys


def fetch_city_weather(city_name: str, api_key: str) -> dict:
    """
    Fetch weather details for a given city using the OpenWeatherMap API.

    Args:
        city_name: Name of the city to fetch the weather for.
        api_key: API key for authenticating with the weather service.

    Returns:
        JSON response payload as a Python dictionary.
        
    Raises:
        ValueError: If city_name or api_key is empty, or if API returns an error.
        requests.exceptions.RequestException: For network-related errors.
        Exception: For other unexpected errors.
    """
    # Validate input parameters
    if not city_name or not city_name.strip():
        raise ValueError("City name cannot be empty")
    if not api_key or not api_key.strip():
        raise ValueError("API key cannot be empty")
    
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name.strip(),
        "appid": api_key.strip(),
        "units": "metric",
    }
    
    try:
        # Make API request with timeout
        response = requests.get(base_url, params=params, timeout=10)
        
        # Check HTTP status code
        response.raise_for_status()
        
        # Parse JSON response
        try:
            weather_data = response.json()
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON response from API: {str(e)}")
        
        # Check if API returned an error message
        if "cod" in weather_data and weather_data["cod"] != 200:
            error_message = weather_data.get("message", "Unknown error")
            raise ValueError(f"API Error: {error_message}")
        
        return weather_data
        
    except requests.exceptions.Timeout:
        raise requests.exceptions.RequestException("Request timed out. Please check your internet connection.")
    except requests.exceptions.ConnectionError:
        raise requests.exceptions.RequestException("Connection error. Please check your internet connection.")
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            raise ValueError(f"City '{city_name}' not found. Please check the city name.")
        elif response.status_code == 401:
            raise ValueError("Invalid API key. Please check your API key.")
        else:
            raise requests.exceptions.RequestException(f"HTTP Error {response.status_code}: {str(e)}")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Request failed: {str(e)}")
    except Exception as e:
        raise Exception(f"Unexpected error occurred: {str(e)}")


def display_weather_details(city_name: str, api_key: str) -> None:
    """
    Display weather details for a city in a user-friendly format.
    
    Args:
        city_name: Name of the city to fetch the weather for.
        api_key: API key for authenticating with the weather service.
    """
    try:
        weather_data = fetch_city_weather(city_name, api_key)
        
        # Extract weather information
        city = weather_data.get("name", "Unknown")
        country = weather_data.get("sys", {}).get("country", "Unknown")
        temperature = weather_data.get("main", {}).get("temp", "N/A")
        feels_like = weather_data.get("main", {}).get("feels_like", "N/A")
        humidity = weather_data.get("main", {}).get("humidity", "N/A")
        pressure = weather_data.get("main", {}).get("pressure", "N/A")
        temp_min = weather_data.get("main", {}).get("temp_min", "N/A")
        temp_max = weather_data.get("main", {}).get("temp_max", "N/A")
        description = weather_data.get("weather", [{}])[0].get("description", "N/A").title()
        wind_speed = weather_data.get("wind", {}).get("speed", "N/A")
        wind_direction = weather_data.get("wind", {}).get("deg", "N/A")
        visibility = weather_data.get("visibility", "N/A")
        cloudiness = weather_data.get("clouds", {}).get("all", "N/A")
        
        # Display weather details in user-friendly format
        print("\n" + "=" * 60)
        print(f"           WEATHER DETAILS FOR {city.upper()}, {country}")
        print("=" * 60)
        print(f"\n📍 Location: {city}, {country}")
        print(f"🌡️  Temperature: {temperature}°C")
        print(f"🤔 Feels Like: {feels_like}°C")
        print(f"📊 Temperature Range: {temp_min}°C - {temp_max}°C")
        print(f"☁️  Condition: {description}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️  Wind Speed: {wind_speed} m/s", end="")
        if wind_direction != "N/A":
            print(f" (Direction: {wind_direction}°)")
        else:
            print()
        print(f"📉 Pressure: {pressure} hPa")
        if visibility != "N/A":
            visibility_km = visibility / 1000
            print(f"👁️  Visibility: {visibility_km} km")
        else:
            print(f"👁️  Visibility: {visibility}")
        print(f"☁️  Cloudiness: {cloudiness}%")
        print("=" * 60 + "\n")
        
    except ValueError as e:
        print("\n" + "❌ " + "=" * 58)
        print("                    ERROR OCCURRED")
        print("=" * 60)
        print(f"\n⚠️  Validation Error: {str(e)}")
        print("\n💡 Please check:")
        print("   - City name is correct and not empty")
        print("   - API key is valid")
        print("=" * 60 + "\n")
        sys.exit(1)
        
    except requests.exceptions.RequestException as e:
        print("\n" + "❌ " + "=" * 58)
        print("                    ERROR OCCURRED")
        print("=" * 60)
        print(f"\n⚠️  Network Error: {str(e)}")
        print("\n💡 Please check:")
        print("   - Your internet connection")
        print("   - The API service is accessible")
        print("=" * 60 + "\n")
        sys.exit(1)
        
    except Exception as e:
        print("\n" + "❌ " + "=" * 58)
        print("                    ERROR OCCURRED")
        print("=" * 60)
        print(f"\n⚠️  Unexpected Error: {str(e)}")
        print("\n💡 Please try again later or contact support.")
        print("=" * 60 + "\n")
        sys.exit(1)


def test_fetch_city_weather():
    """Test cases for fetch_city_weather function."""
    api_key = "ff6aa4c18255076bae9b5ee8fb0048d8"
    
    # Test case 1: Empty city name should raise ValueError
    print("Test 1: Empty city name validation")
    try:
        fetch_city_weather("", api_key)
        assert False, "Should raise ValueError for empty city name"
    except ValueError as e:
        assert "empty" in str(e).lower(), "Error message should mention empty"
        print("✓ Test 1 passed: ValueError raised for empty city name")
    
    # Test case 2: City name with whitespace should be handled correctly
    print("\nTest 2: City name with whitespace")
    weather_data = fetch_city_weather("  warangal  ", api_key)
    assert isinstance(weather_data, dict), "Should return a dictionary"
    assert "name" in weather_data, "Should contain 'name' key"
    print("✓ Test 2 passed: Whitespace handled correctly")
    
    # Test case 3: Valid city should return complete weather data structure
    print("\nTest 3: Complete weather data structure")
    weather_data = fetch_city_weather("mumbai", api_key)
    assert isinstance(weather_data, dict), "Should return a dictionary"
    assert "name" in weather_data, "Should contain 'name' key"
    assert "main" in weather_data, "Should contain 'main' key"
    assert "temp" in weather_data["main"], "Main should contain 'temp'"
    assert "humidity" in weather_data["main"], "Main should contain 'humidity'"
    assert "pressure" in weather_data["main"], "Main should contain 'pressure'"
    assert "weather" in weather_data, "Should contain 'weather' key"
    assert len(weather_data["weather"]) > 0, "Weather array should not be empty"
    print("✓ Test 3 passed: Complete data structure returned")
    
    print("\n✅ All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    print("="*50)
    print("Running test cases...")
    print("="*50)
    test_fetch_city_weather()
    
    # Example usage
    print("\n" + "="*50)
    print("Example usage:")
    print("="*50)
    city_name = "Warangal"
    api_key = "ff6aa4c18255076bae9b5ee8fb0048d8"
    display_weather_details(city_name, api_key)

