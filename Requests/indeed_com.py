import requests
from bs4 import BeautifulSoup as bs


def extract(page):
    headers = {'User-Agent' : ' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    url = f'https://eg.indeed.com/jobs?q=python%20developer&start={page}&vjk=ab9eca08d78e44fc'
    r = requests.get(url, headers)
    soup = bs(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_='cardOutline')
    return len(divs)


c = extract(0)
print(transform(c))