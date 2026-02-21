import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

URL = "https://dpboss.boston/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
response = requests.get(URL, headers=headers, timeout=20)
soup = BeautifulSoup(response.text, 'html.parser')

all_data = []
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
    
    block_text = h4.get_text("|", strip=True)
    for sibling in h4.find_next_siblings():
        if sibling.name == 'h4':
            break
        block_text += "|" + sibling.get_text("|", strip=True)
    
    parts = block_text.split("|")
    result_str = ""
    times_str = ""
    
    for part in parts:
        part_strip = part.strip()
        # OLD REGEX: r'[\d\*]{3}-[\d\*]{1,2}-?[\d\*]{0,3}'
        if re.search(r'[\d\*]{3}-[\d\*]{1,2}', part_strip):
            result_str = part_strip
        elif re.search(r'\d{1,2}:\d{2}', part_strip):
            times_str = part_strip
            
    open_panna = ""
    main_jodi = ""
    close_panna = ""
    
    if result_str:
        # Improved extraction
        res_match = re.search(r'([\d\*]{3})\s*-\s*([\d\*]{1,2})(?:\s*-\s*([\d\*]{0,3}))?', result_str)
        if res_match:
            open_panna = res_match.group(1)
            main_jodi = res_match.group(2)
            close_panna = res_match.group(3) if res_match.group(3) else ""

    if "PARVATI" in name.upper() or "MAHADEVI" in name.upper():
        print(f"Name: {name}")
        print(f"Result Str: {result_str}")
        print(f"Open: {open_panna}, Main: {main_jodi}, Close: {close_panna}")
        print("-" * 20)
