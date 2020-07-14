from sys import argv
from bs4 import BeautifulSoup
import requests


class ImgSearch:
    # input string, a search term used for finding thumbnail
    # return string, url of thumbnail image
    def search(self, term):
        url = "https://www.google.com/search?q="+ term +"&tbm=isch"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        src = soup.select('img')[1].get('src')
        return src

imgs = ImgSearch()

if __name__ == "__main__":
    if len(argv) > 1:
        symbols = argv[1:]
        for term in symbols:
            testresult = imgs.search(term)
            print(testresult)