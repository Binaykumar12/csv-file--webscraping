import requests
from bs4 import BeautifulSoup
import random
import time

url="https://www.tutorialsfreak.com/"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.content,"lxml")
# print(soup)

