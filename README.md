# **google thumbnail image query**

## === Purpose === 
Get the src of the first thumbnail found on google image


## === Function === 
Makes a search for the argument on google images and parse out the src from the first image


## === Dependencies ===
RUN to install libraries
```
pip install -r requirements.txt
```
[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)


## === Image Search Usage === 

python3 imgsearch.py [search term]

```
python3 imgsearch.py '2015 toyota corolla'    
```
Result
```
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSonJxAfFZ1sX8BQzMBYumipvihwJBc_0s30cem1zikjmsNppRo1V-eSFM
```


## === Run Example Flask Project === 
Start Server
```
python3 app.py
```


## === Running on Docker === 
Build container
```
docker build -t thumbsearch .
```
Run container
```
docker run -p 5000:5000 thumbsearch
```

