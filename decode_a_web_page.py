import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
for title in soup.find_all('h3'):
    print(title.get_text())

