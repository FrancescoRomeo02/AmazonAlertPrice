import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.8', }

url = "https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08QMB94YW/ref=sr_1_4?keywords=macbook+air+m1&qid=1656171544&sr=8-4"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.h1.text
price = soup.find(
    'span', {'class': 'a-price a-text-price a-size-medium'}).text

with open('price_tracker.csv', 'w') as f:
    f.write(title + '\n')
    f.write(price.split('$')[1])
    f.close()
