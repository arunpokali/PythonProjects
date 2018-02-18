import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages :
        url = 'https://in.bookmyshow.com/hyderabad/movies/telugu/'
        source_code = requests.get(url)

        plain_txt = source_code.text

        soup = BeautifulSoup(plain_txt, "html.parser")

        for link in soup.find_all('a'):
            #href = 'https://in.bookmyshow.com' +link.get('href')
            #print(href)
            #print(link.string)
            if link.string == 'Gentleman':
               #print(link.string)
               goto_link('https://in.bookmyshow.com' +link.get('href'))
               #goto_link(href)

        page += 1

def goto_link(url):

    print(url)
    source_code = requests.get(url)

    plain_txt = source_code.text

    soup = BeautifulSoup(plain_txt, "html.parser")

    for link in soup.find_all('a'):
            href ='https://in.bookmyshow.com' + link.get('href')
            print(href)
            print(link.string)






trade_spider(1)