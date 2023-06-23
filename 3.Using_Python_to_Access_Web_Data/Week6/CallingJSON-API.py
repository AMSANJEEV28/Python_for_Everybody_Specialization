import urllib.parse
import urllib.request
import json

# API endpoint URL
base_url = 'http://py4e-data.dr-chuck.net/json?'

# Prompt for a location
location = input('Enter location: ')

# Construct the API request URL
params = {
    'address': location,
    'key': 42  # Replace with your own key if necessary
}
url = base_url + urllib.parse.urlencode(params)

print('Retrieving', url)

# Call the API and retrieve the JSON response
response = urllib.request.urlopen(url)
data = response.read().decode()

print('Retrieved', len(data), 'characters')

# Parse the JSON response
try:
    json_data = json.loads(data)
except:
    json_data = None

# Extract the place_id from the JSON if available
if json_data and 'results' in json_data:
    place_id = json_data['results'][0]['place_id']
    print('Place ID', place_id)
else:
    print('No place ID found')
