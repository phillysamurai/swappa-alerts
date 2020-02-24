from bs4 import BeautifulSoup
import requests

price_list = []


def grab_prices(url):
    headers = {'user-agent': 'my-app/0.0.1'}
    source = requests.get(url, headers=headers).text
    url_parse = BeautifulSoup(source, 'lxml')
    for section_main in url_parse.find_all(id='section_main'):
        for seller_info in section_main.find_all('div', class_='seller_info'):
            for price in seller_info.find_all('span', class_='price'):
                parse = price.text
                parse_split = parse.split('$')[1]
                price_list.append(parse_split)
    return price_list
