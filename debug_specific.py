import requests
from bs4 import BeautifulSoup
import re

URL = "https://dpboss.boston/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
response = requests.get(URL, headers=headers, timeout=20)
soup = BeautifulSoup(response.text, 'html.parser')

print("--- SEARCHING FOR PARVATI AND MAHADEVI ---")
start_collecting = False
h4_tags = soup.find_all('h4')
for h4 in h4_tags:
    name = h4.get_text(strip=True)
    
    if "WORLD ME SABSE FAST" in name.upper():
        start_collecting = True
        continue
    
    if not start_collecting:
        continue

    if any(stop_word in name.upper() for stop_word in ["FREE GAME", "JODI LIST", "CHART LIST", "GUESSING"]):
        break
    
    if "PARVATI" in name.upper() or "MAHADEVI" in name.upper():
        print(f"\nFound Market: {name}")
        block_text = h4.get_text("|", strip=True)
        for sibling in h4.find_next_siblings():
            if sibling.name == 'h4':
                break
            block_text += "|" + sibling.get_text("|", strip=True)
        print(f"Full Block Text: {block_text}")
        
print("--- END OF SEARCH ---")
