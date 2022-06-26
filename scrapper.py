import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.8', }

search_query = 'macbook air m1'.replace(' ', '+')
base_url = f'https://www.amazon.com/s?k={search_query}'

items = []

for i in range(0, 1):
    url = base_url + f'&page{i}'
    print(url)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all(
        'div', {'class': 's-result-item', 'data-component-type': 's-search-result'})

    for result in results:
        try:
            title = result.h2.text
        except AttributeError:
            continue
        try:
            rating = result.find('i', {'class': 'a-icon'}).text
        except AttributeError:
            rating = 'N/A'
            continue
        try:
            price1 = result.find('span', {'class': 'a-price-whole'}).text
            price2 = result.find('span', {'class': 'a-price-fraction'}).text
            price = f'{price1}{price2}'
        except AttributeError:
            price = 'N/A'
            continue
        try:
            link = 'https://www.amazon.com' + result.h2.a['href']
        except AttributeError:
            link = 'N/A'
            continue
        items.append({'title': title, 'rating': rating,
                     'price': price, 'link': link})

for item in items:
    # scrive i dati nel file
    with open('data.csv', 'a') as f:
        f.write(
            f'{item["title"]}\n{item["rating"]}\n{item["price"]}\n{item["link"]}\n\n')
