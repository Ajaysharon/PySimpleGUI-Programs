import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    page=requests.get(url).content
    return page

def parse_html_page(page,tag):
    data=[]
    soup=BeautifulSoup(page,'html.parser')
    for para in soup.find_all(tag):
        data.append(para.text)

    return data

if __name__=='__main__':
    url='https://realpython.com/beautiful-soup-web-scraper-python/'
    page=get_html_content(url)
    print(parse_html_page(page,'p'))
