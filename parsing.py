from bs4 import BeautifulSoup
from time import sleep
import requests

headers = {'User-Agent':
           'Mozilla/5.0 (X11; Linux i686; rv:2.0.1)'
           'Gecko/20100101 Firefox/4.0.1'}


def geturl():
    for numb in range(1, 8):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={numb}'

        request = requests.get(url, headers=headers)
        htmlcode = BeautifulSoup(request.text, 'lxml')

        card = htmlcode.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for a in card:
            cardurl = 'https://scrapingclub.com' + a.find('a').get('href')
            yield cardurl


for cardurl in geturl():
    sleep(3)
    request = requests.get(cardurl, headers=headers)
    htmlcode = BeautifulSoup(request.text, 'lxml')

    card = htmlcode.find('div', class_='card mt-4 my-4')
    name = card.find('h3', class_='card-title').text
    price = card.find('h4').text
    urlimg = 'https://scrapingclub.com' + card.find('img', class_='card-img-top img-fluid').get('src')
    text = card.find('p', class_='card-text').text
    print(name + '\n' + price + '\n' + urlimg + '\n' + text + '\n\n')
