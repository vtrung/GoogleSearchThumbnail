from sys import argv
from imgsearch import ImgSearch
from flask import Flask

app = Flask(__name__)
imgs = ImgSearch()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/search/<term>')
def search_term(term = None):
    if term == None:
        return "Not Found"
    else:
        print(term)
        result = imgs.search(term)
        return result

# if __name__ == "__main__":
#     if len(argv) > 1:
#         symbols = argv[1:]
#         for term in symbols:
#             testresult = imgs.search(term)
#             print(testresult)


if __name__ == '__main__':
    app.run()