import requests
from bs4 import BeautifulSoup
import random
import time

url="https://www.tutorialsfreak.com/"
r=requests.get(url)
# print(r)

soup=BeautifulSoup(r.content,"lxml")
# print(soup)

title= soup.find_all("a",class_ ="fs-20 lh-30 fw-500 label-color-5 mb-3")
print(title)
