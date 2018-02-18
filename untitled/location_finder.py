import re
import sys
import requests
from bs4 import BeautifulSoup

usage = "Run the script: ./geolocate.py IPAddress"

ipaddr = input("enter ip")

geody = "http://www.geody.com/geoip.php?ip=" + ipaddr
print(geody)
html_page = requests.get(geody)
soup = BeautifulSoup(html_page.text, "html.parser")

# Filter paragraph containing geolocation info.
paragraph = soup('p')[3]

print(paragraph)

# Remove html tags using regex.
geo_txt = re.sub(r'<.*?>', '', str(paragraph))
print(geo_txt[32:].strip())