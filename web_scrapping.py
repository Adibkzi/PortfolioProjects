from urllib.request import urlopen
from bs4 import BeautifulSoup

# website 
url_to_scrape = 'https://planetdesert.com/collections/cactus'

request_page = urlopen(url_to_scrape)

page_html = request_page.read()
request_page.close()

# Soup needed 
html_soup = BeautifulSoup(page_html, 'html.parser')

cactus_items  = html_soup.find_all('div', class_="grid-product_content")

filename = 'products.csv'
f = open(filename, 'w')

headers = 'Title, Price \n'

f.write(headers)
# loop 
for cactus in cactus_items:
    title = cactus.find('div', class_="grid-product_title").text
    price = cactus.find('div', class_="grid-product_price").text
    
    f.write(title + ',' + price)

f.close()

