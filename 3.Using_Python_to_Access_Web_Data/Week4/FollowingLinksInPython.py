import urllib.request
from bs4 import BeautifulSoup

def retrieve_url(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_next_link(soup, position):
    tags = soup('a')
    if len(tags) < position:
        return None
    next_link = tags[position - 1].get('href')
    return next_link

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

for i in range(count):
    print("Retrieving:", url)
    soup = retrieve_url(url)
    next_link = get_next_link(soup, position)
    if not next_link:
        break
    url = next_link

print("The answer to the assignment is:", url)
