import requests
from bs4 import BeautifulSoup as bs

def extract(page):
    url = f'https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067?_pgn={page}'
    headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0'
    }