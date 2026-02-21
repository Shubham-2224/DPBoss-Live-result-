import requests
from bs4 import BeautifulSoup
import re

URL = "https://dpboss.boston/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all buttons or divs that look like market blocks
blocks = soup.find_all('div', class_=re.compile(r'result|market|box|card', re.I))
print(f"Total potential market blocks: {len(blocks)}")

# Let's count how many have an h4 inside
h4_blocks = [b for b in blocks if b.find('h4')]
print(f"Blocks with h4 inside: {len(h4_blocks)}")

# Let's see the 3rd table again. 19 rows. 
# Maybe the user means a literal table that I missed?
# Some sites have a "Live Results Table" at the bottom.
tables = soup.find_all('table')
for i, t in enumerate(tables, 1):
    rows = len(t.find_all('tr'))
    print(f"Table {i}: {rows} rows")
    if rows > 100:
        print(f"FOUND LARGE TABLE: Table {i}")
