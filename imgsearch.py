from sys import argv
from bs4 import BeautifulSoup
import requests


class ImgSearch:
    def test(self):
        print("testing 1")
    
    # input string, a search term used for finding thumbnail
    # return string, url of thumbnail image
    def search(self, term):
        url = "https://www.google.com/search?q="+ term +"&tbm=isch"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        src = soup.select('#search img')[0].get('src')
        return src

