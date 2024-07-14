import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd

# URL of the page to scrape
url = "https://quotes.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
for quote in quotes:
    print(quote.text)

authors = soup.find_all("small", class_="author")
for author in authors:
    print(author.text)

quote_texts = [quote.text for quote in quotes]
author_names = [author.text for author in authors]

data = {
    "Author": author_names,
    "Quote": quote_texts
    
}
df = pd.DataFrame(data)
excel_filename = "quotes.xlsx"
df.to_excel(excel_filename, index=False)

# Sleep for a random interval between 1 and 3 seconds
s = random.uniform(1, 3)
print(f"Sleeping for {s:.2f} seconds")
time.sleep(s)