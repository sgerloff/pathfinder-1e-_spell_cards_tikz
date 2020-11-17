from pyquery import PyQuery
import requests

def getTextFromURL( url ):
    req = requests.get(url)
    pq = PyQuery(req.text)
    tag = pq('div#page.page')
    return tag
