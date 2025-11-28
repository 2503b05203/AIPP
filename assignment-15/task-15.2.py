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
        ValueError: If city_name or api_key is empty.
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


def display_weather_json(city_name: str, api_key: str) -> None:
    """
    Display weather details for a city as formatted JSON output.
    
    Args:
        city_name: Name of the city to fetch the weather for.
        api_key: API key for authenticating with the weather service.
    """
    try:
        weather_data = fetch_city_weather(city_name, api_key)
        
        # Display weather details as formatted JSON
        json_output = json.dumps(weather_data, indent=4, ensure_ascii=False)
        print("Weather Details (JSON):")
        print("=" * 50)
        print(json_output)
        print("=" * 50)
        
    except ValueError as e:
        error_response = {
            "error": "Validation Error",
            "message": str(e)
        }
        print(json.dumps(error_response, indent=4))
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        error_response = {
            "error": "Network Error",
            "message": str(e)
        }
        print(json.dumps(error_response, indent=4))
        sys.exit(1)
    except Exception as e:
        error_response = {
            "error": "Unexpected Error",
            "message": str(e)
        }
        print(json.dumps(error_response, indent=4))
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
    
    # Test case 2: Empty API key should raise ValueError
    print("\nTest 2: Empty API key validation")
    try:
        fetch_city_weather("warangal", "")
        assert False, "Should raise ValueError for empty API key"
    except ValueError as e:
        assert "empty" in str(e).lower() or "api key" in str(e).lower(), "Error message should mention empty API key"
        print("✓ Test 2 passed: ValueError raised for empty API key")
    
    # Test case 3: Valid city name should return dictionary with required keys
    print("\nTest 3: Valid city name returns proper structure")
    weather_data = fetch_city_weather("warangal", api_key)
    assert isinstance(weather_data, dict), "Should return a dictionary"
    assert "name" in weather_data, "Should contain 'name' key"
    assert "main" in weather_data, "Should contain 'main' key"
    assert "weather" in weather_data, "Should contain 'weather' key"
    assert "sys" in weather_data, "Should contain 'sys' key"
    print("✓ Test 3 passed: Valid response structure")
    
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
    city_name = "warangal"
    api_key = "ff6aa4c18255076bae9b5ee8fb0048d8"
    display_weather_json(city_name, api_key)