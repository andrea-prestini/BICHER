import requests
from bs4 import BeautifulSoup

# Send a GET request to the website and retrieve the HTML content
url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

book_containers = soup.find_all("article", class_="product_pod")
for container in book_containers:
    title = container.h3.a.text
    price = container.find("div", class_="product_price").p.text
    print(title, price)
