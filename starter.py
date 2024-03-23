"""
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd



url = "https://jgsj.jayagrocer.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
productlinks = []
for x in range(1,20):
    k = requests.get('https://jgsj.jayagrocer.com/search?type=product&options%5Bprefix%5D=last&q=greek+yogurt&page={}'.format(x)).text
    soup = BeautifulSoup(k, 'html.parser')
    productlist = soup.find_all("a", {"class":"product-item__title text--strong link"})
    for product in productlist:
            link = product.get("href")               
            productlinks.append(url+link)

print(productlinks)