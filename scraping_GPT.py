import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find_all('article')
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').get_text()
    print(f'Title: {title} / Price: {price}')
