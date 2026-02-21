import requests
from bs4 import BeautifulSoup
import re

URL = "https://dpboss.boston/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
response = requests.get(URL, headers=headers, timeout=20)
soup = BeautifulSoup(response.text, 'html.parser')

print("--- START OF LIVE RESULT INSPECTION ---")
start_collecting = False
h4_tags = soup.find_all('h4')
count = 0
for h4 in h4_tags:
    name = h4.get_text(strip=True)
    if "WORLD ME SABSE FAST" in name.upper():
        start_collecting = True
        continue
    if not start_collecting:
        continue
    if any(stop_word in name.upper() for stop_word in ["FREE GAME", "JODI LIST", "CHART LIST", "GUESSING"]):
        break
    
    count += 1
    if count > 5: break # Only check first 5
    
    print(f"\nMarket Name: {name}")
    parent = h4.find_parent('div')
    if parent:
        print(f"Parent Div Content: {parent.get_text('|', strip=True)}")
        # Check siblings if not in parent
        print("Checking siblings of H4:")
        for sibling in h4.next_siblings:
            if sibling.name:
                print(f"  <{sibling.name}>: {sibling.get_text(strip=True)}")
            if count > 5: break
print("--- END OF INSPECTION ---")
