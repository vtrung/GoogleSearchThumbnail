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
        result = imgs.search(term)
        return "<img src='{}'/>".format(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)