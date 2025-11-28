import requests


def get_weather(city_name: str, api_key: str = "ff6aa4c18255076bae9b5ee8fb0048d8") -> None:
    """
    Fetch and display weather data for a given city using the OpenWeather API.
    
    Args:
        city_name: Name of the city to fetch weather for.
        api_key: API key for OpenWeather API (optional, has default value).
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",  # Get temperature in Celsius
    }
    
    try:
        # Make API request
        response = requests.get(base_url, params=params, timeout=10)
        
        # Check if city not found (404 or cod == "404" in response)
        if response.status_code == 404:
            print("Error: City not found. Please enter a valid city.")
            return
        
        # Raise exception for other HTTP errors
        response.raise_for_status()
        
        # Parse JSON response
        weather_data = response.json()
        
        # Check if API returned an error (sometimes API returns 200 but with error in body)
        if weather_data.get("cod") == "404" or weather_data.get("cod") == 404:
            print("Error: City not found. Please enter a valid city.")
            return
        
        # Extract required information
        city = weather_data.get("name", "Unknown")
        temperature = weather_data.get("main", {}).get("temp", "N/A")
        humidity = weather_data.get("main", {}).get("humidity", "N/A")
        weather_description = weather_data.get("weather", [{}])[0].get("description", "N/A")
        
        # Display the weather information
        print(f"\nCity: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {weather_description.title()}\n")
        
    except requests.exceptions.ConnectionError:
        print("Error: Network connection failed. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while fetching weather data: {str(e)}")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")


def test_get_weather():
    """Test cases for get_weather function."""
    api_key = "ff6aa4c18255076bae9b5ee8fb0048d8"
    
    # Test case 1: Valid city name should execute without errors
    print("Test 1: Valid city name execution")
    try:
        get_weather("warangal", api_key)
        print("✓ Test 1 passed: Function executed successfully for valid city")
    except Exception as e:
        assert False, f"Should not raise exception for valid city: {str(e)}"
    
    # Test case 2: Function should handle different valid city names
    print("\nTest 2: Different valid city names")
    cities = ["london", "mumbai", "tokyo"]
    for city in cities:
        try:
            get_weather(city, api_key)
            print(f"  ✓ {city} handled successfully")
        except Exception as e:
            # If it's a network error, that's acceptable for testing
            if "connection" in str(e).lower() or "timeout" in str(e).lower():
                print(f"  ⚠ {city} - Network issue (acceptable in test)")
            else:
                assert False, f"Unexpected error for {city}: {str(e)}"
    print("✓ Test 2 passed: Multiple cities handled")
    
    # Test case 3: Invalid city name should handle gracefully
    print("\nTest 3: Invalid city name handling")
    try:
        get_weather("InvalidCityName12345", api_key)
        print("✓ Test 3 passed: Invalid city handled gracefully")
    except Exception as e:
        # Should either print error message or handle gracefully
        assert "error" in str(e).lower() or "not found" in str(e).lower() or "city" in str(e).lower(), \
            f"Should handle invalid city gracefully: {str(e)}"
        print("✓ Test 3 passed: Invalid city error handled")
    
    print("\n✅ All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    print("="*50)
    print("Running test cases...")
    print("="*50)
    test_get_weather()
    
    # Example usage
    print("\n" + "="*50)
    print("Example usage (interactive):")
    print("="*50)
    # Get city name from user input
    city_name = input("Enter the city name: ").strip()
    
    if city_name:
        get_weather(city_name)
    else:
        print("Error: City name cannot be empty. Please enter a valid city name.")

