import urllib.request
import xml.etree.ElementTree as ET

# Prompt for the URL
url = input("Enter location: ")

# Read the XML data from the URL
xml_data = urllib.request.urlopen(url).read()

# Parse the XML data 
tree = ET.fromstring(xml_data)

# Find all the count elements using XPath
counts = tree.findall('.//count')

# Compute the sum of the numbers
total = sum(int(count.text) for count in counts)

# Print the result
print("Sum:", total)
