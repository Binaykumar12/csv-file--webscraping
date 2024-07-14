import requests
from bs4 import BeautifulSoup
import random
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

url = "https://www.tutorialsfreak.com/"

# Function to make a request and handle potential issues
def fetch_page(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Fetch the page content
page_content = fetch_page(url, headers)

if page_content:
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(page_content, "lxml")

    # Find all titles with the specified class
    titles = soup.find_all("a", class_="fs-20 lh-30 fw-500 label-color-5 mb-3")

    # Print the titles
    for title in titles:
        print(title.get_text(strip=True))
else:
    print("Failed to retrieve the webpage content.")
