import requests
from bs4 import BeautifulSoup as bs
import pandas as bd

def extract(page):
    url = f'https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067?_pgn={page}'
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0'
    }
    r = requests.get(url, headers=headers)
    #print(r)
    soup = bs(r.content, 'html.parser')
    return soup
def parse(soup):
    divs = soup.find_all('div', class_='s-item s-item--large')
    return len(divs)
print('hi')
c = extract(1)
print(c.prettify)
parsed=parse(c)
print(parsed)
