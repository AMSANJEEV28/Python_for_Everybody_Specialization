import urllib.request
import json

url = input("Enter location: ")
print("Retrieving", url)

# Read the JSON data from the URL
data = urllib.request.urlopen(url).read().decode()
print("Retrieved", len(data), "characters")

# Parse the JSON data
json_data = json.loads(data)

# Extract the comment counts
comment_counts = [comment['count'] for comment in json_data['comments']]

# Compute the sum of the comment counts
total_sum = sum(comment_counts)

# Display the count and sum
print("Count:", len(comment_counts))
print("Sum:", total_sum)
