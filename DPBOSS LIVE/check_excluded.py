import requests
from bs4 import BeautifulSoup

URL = "https://dpboss.boston/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

all_names = []
start_counting = False
for h4 in soup.find_all('h4'):
    name = h4.get_text(strip=True)
    if "WORLD ME SABSE FAST" in name.upper():
        start_counting = True
        continue
    if start_counting:
        all_names.append(name)

for i, name in enumerate(all_names, 1):
    print(f"{i}: {name}")
