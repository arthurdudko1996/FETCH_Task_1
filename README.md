FETCH_Task_1

Geolocation Utility
This command-line utility fetches latitude, longitude,and place information based on 
city/state or ZIP code inputs using the OpenWeather Geocoding API.
It works within the United States.

Features:
Supports both city/state and ZIP code inputs.
Handles multiple locations at once.

Prerequisites:
Python 3.x: Make sure Python is installed. You can download it from python.org.

Ensure the requests library is installed:

pip install requests


API Key: The API key is already included.

Setup:

Clone the Repository:
git clone <repository-url>
cd FETCH_Test

How to Run:

To use the utility, provide locations (city/state or ZIP codes) as command-line arguments:

Single Value Example:

python geoloc_util.py --locations "Madison, WI" "90210"

Multiple Value Example:

python geoloc_util.py --locations "Madison, WI" "90210" "New York, NY"

Example Output:

{'name': 'Madison', 'state': 'Wisconsin', 'lat': 43.074761, 'lon': -89.3837613, 'country': 'US'}

{'name': 'Beverly Hills', 'lat': 34.0901, 'lon': -118.4065, 'country': 'US'}

{'name': 'New York County', 'state': 'New York', 'lat': 40.7127281, 'lon': -74.0060152, 'country': 'US


Running the Tests:

To run the integration tests, execute the following command:

pytest tests/test_geoloc_util.py

Example Output
If the tests pass, you should see output like this:

============================= test session starts ==============================
collected 9 items

tests/test_geoloc_util.py ......                                           [100%]

============================== 6 passed in 0.72s ===============================


