from sys import argv
from bs4 import BeautifulSoup
import requests
import threading

if __name__ == "__main__":
    if len(argv) > 1:
        symbols = argv[1:]
        for symbol in symbols:
            term = "2015 Corolla"
            url = "https://www.google.com/search?q="+ symbol +"&tbm=isch"
            r = requests.get(url)
            #print(r.text)
            soup = BeautifulSoup(r.text, "html.parser")
            src = soup.select('#search img')[0].get('src')
            print(src)