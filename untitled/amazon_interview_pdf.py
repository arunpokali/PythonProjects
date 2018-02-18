import httplib2
import pdfcrowd
from bs4 import BeautifulSoup, SoupStrainer
#import http.client

http = httplib2.Http()
s = 'http://www.geeksforgeeks.org/tag/amazon/'
ii = 0

to_crawl = []
crawled = []
to_crawl.append(s)
status, response = http.request(s)
crawled.append(s)

for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        li = link['href']
        # print(li)
        if li.find('http://www.geeksforgeeks.org') == 0 and li not in crawled and li.find('forums') < 0 < li.find(
                'amazon'):
            to_crawl.append(li)

# print (to_crawl)
print(len(to_crawl))
count = 0


def get_page(page):
    #import http.client

    print('page', page)
    source = BeautifulSoup(page,'html.parser')
    #source.request("GET", "/")
    # source.request('GET')
    resp = source.get_text()
    print(resp)
    #while not resp.closed:
     #   print("source", resp.read(200))
    #return resp.read()


def save_as_pdf(s):
    global ii
    try:
        print("entered save as pdf")
        client = pdfcrowd.Client("mkap1234", "fc5ada9fbd1c55f46822d6e9e985a9bb")
        output_file = open('amazon' + str(ii) + '.pdf', 'wb')
        ii += 1
        print("calling getpage", s)
        html = get_page(s)
        print("html", html)
        client.convertHtml(html, output_file)
        output_file.close()
    except pdfcrowd.Error as why:
        print('Failed:', why)


i = 10

while i > 0:
    b = to_crawl.pop()
    print(b)
    if b.find('http://www.geeksforgeeks.org') == 0 and b not in crawled and b.find('forums') < 0 < li.find(
            'amazon'):
        count = count + 1
        print(count, b)
        crawled.append(b)
        status, response = http.request(b)
        for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
            if link.has_attr('href'):
                li = link['href']
                print(li)
                if b.find('http://www.geeksforgeeks.org') == 0 and li not in crawled:
                    to_crawl.append(li)
    i -= 1
    print('i', i)

amazon = []

print("crawled", crawled)
print('to crawl', len(to_crawl), to_crawl)

for st in to_crawl:
    if st.find('amazon') >= 0 > st.find('#') and st.find('tag') < 0 and st.find('forum') < 0:
        print('st', st)
        amazon.append(st)

print("Finished")
print(len(amazon))

for page in amazon:
    print(page)
    save_as_pdf(page)
