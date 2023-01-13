import requests
from bs4 import BeautifulSoup
import csv


# Send a GET request to the website and retrieve the HTML content
url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
book_containers = soup.find_all("article", class_="product_pod")

# Open a CSV file for writing
with open("books.csv", "w", newline='', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Title", "Price", "Link"])

    for container in book_containers:
        title = container.h3.a.text
        price = container.find("div", class_="product_price").p.text
        link = container.h3.a["href"]
        print(title, price, link)
        writer.writerow([title, price, link])
