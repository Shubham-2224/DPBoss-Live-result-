import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

URL = "https://dpboss.boston/"

def scrape_data():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        response = requests.get(URL, headers=headers, timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

    all_data = []
    for h4 in soup.find_all('h4'):
        name = h4.get_text(strip=True)
        if any(keyword in name.upper() for keyword in ["MORNING", "DAY", "NIGHT", "KALYAN", "BAZAR", "TIME", "MUMBAI"]):
            if "WORLD ME" in name or "DPBOSS" in name:
                continue
            all_data.append(name)
    return all_data

names = scrape_data()
print("Scraped names (first 10):", names[:10])
