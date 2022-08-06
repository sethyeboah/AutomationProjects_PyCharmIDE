from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import requests

page = requests.get("https://coinmarketcap.com/currencies/bitcoin/")

soup = bs(page.content, 'html.parser')

# The whole html page
# print(soup)

# Title of the page
print(soup.title)

# Get attributes
print(soup.title.name)

# Get values:
print(soup.title.string)

# Get The Crypto's Price
for div in soup.find_all(class_='sc-16r8icm-0 kjciSH priceTitle'):
    for child_div in div.find_all('div'):
        price = child_div.string

print(price)