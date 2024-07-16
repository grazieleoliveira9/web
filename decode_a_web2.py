import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
for title in soup.find_all('p'):
    print(title.get_text())