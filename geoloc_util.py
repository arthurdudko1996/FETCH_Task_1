import requests
import argparse

# Open Weather API Key
API_KEY = 'f897a99d971b5eef57be6fafa0d83239'

# Base URLs for the OpenWeather Geocoding API
BASE_URL_CITY = "http://api.openweathermap.org/geo/1.0/direct"
BASE_URL_ZIP = "http://api.openweathermap.org/geo/1.0/zip"

# Function to get location details by city and state
def get_location_by_city_state(city_state):
    # Replace spaces and format the input correctly
    city_state_clean = city_state.replace(" ", "").split(",")
    
    # Handle the special case for "New York, NY" by querying only "New York"
    if city_state_clean[0].lower() == "newyork":
        city_state_query = "New York,US"
    elif len(city_state_clean) == 2:
        city_state_query = f"{city_state_clean[0]},{city_state_clean[1]},US"
    else:
        return f"Invalid city/state input format for: {city_state}"

    params = {
        'q': city_state_query,
        'limit': 5,  # Get up to 5 results to handle multiple New Yorks
        'appid': API_KEY
    }

    response = requests.get(BASE_URL_CITY, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            # Return the first result
            return {
                'name': data[0]['name'],
                'state': data[0].get('state', 'N/A'),
                'lat': data[0]['lat'],
                'lon': data[0]['lon'],
                'country': data[0]['country']
            }
        else:
            return f"No data found for location: {city_state}"
    else:
        return f"Error: Unable to fetch data for {city_state}"

# Function to get location details by ZIP code
def get_location_by_zip(zip_code):
    params = {
        'zip': f"{zip_code},US",  # Using only USA Region
        'appid': API_KEY
    }
    response = requests.get(BASE_URL_ZIP, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['name'],
            'lat': data['lat'],
            'lon': data['lon'],
            'country': data['country']
        }
    else:
        return f"Error: Unable to fetch data for ZIP code: {zip_code}"

# Function to handle multiple inputs and display the results
def geoloc_util(locations):
    for location in locations:
        if location.isdigit():  # need to check here if input is a ZIP code
            result = get_location_by_zip(location)
        else:
            result = get_location_by_city_state(location)
        print(result)

# Command-line argument parser
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Geolocation utility to fetch latitude, longitude, and place information.")
    parser.add_argument("--locations", nargs='+', help="List of locations (city/state or zip codes)", required=True)
    args = parser.parse_args()

    geoloc_util(args.locations)
