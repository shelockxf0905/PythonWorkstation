from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys

# Retrieve HTML string from the URL
# html = urlopen("https://www.ixigua.com/?wid_try=1")
# print(html.read())


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.body.title
    except AttributeError as e:
        return None
    return title

title = getTitle("https://kankan.eastday.com/?qid=01365")
if title is None:
    print("Title could not be found")
else:
    print(title)
