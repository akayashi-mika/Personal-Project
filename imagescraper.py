import urllib2
from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://example.com').read())

for row in soup('table', {'class': 'spad'})[0].tbody('tr'):
    tds = row('td')
    print tds[0].string, tds[1].string
    # will print date and sunrise
