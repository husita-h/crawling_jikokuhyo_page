import requests
from bs4 import BeautifulSoup # http://kondou.com/BS4/

vgm_url = 'https://www.city.kita.tokyo.jp/d-shisetu/kurashi/bus/bus.html'
res = requests.get(vgm_url)
soup = BeautifulSoup(res.content, 'html.parser')
print(soup)