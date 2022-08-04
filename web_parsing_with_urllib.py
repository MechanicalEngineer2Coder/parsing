# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

#Get count and position and convert to int
count = input('Enter count: ')
pos = input('Enter position: ')
count = int(count)
pos = int(pos)

print(url)

i = 1
while i <= count:
    print(i, tags[pos-1].get('href'))
    # Ignore SSL certificate errors
    #ctx = ssl.create_default_context()
    #ctx.check_hostname = False
    #ctx.verify_mode = ssl.CERT_NONE

    #Setup next loop
    url = tags[pos-1].get('href')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    #print(i, tags[pos-1].get('href', None))
    i += 1
