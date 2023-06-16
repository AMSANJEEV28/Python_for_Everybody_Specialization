import urllib.request
from bs4 import BeautifulSoup

url = "https://py4e-data.dr-chuck.net/comments_1826229.html"

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
tags = soup('span')
for tag in tags:
    num = int(tag.contents[0])
    sum += num

print("Count:", len(tags))
print("Sum:", sum)
