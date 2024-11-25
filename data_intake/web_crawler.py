import requests
from bs4 import BeautifulSoup

def news_scraper(url):
    news_data = []
    content = []

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    article = soup.find_all('p')
    timestamp = soup.find('span').get_text()
    title = soup.find('h1',id = 'article-0').get_text()

    for i in article[:-3]:
        content.append(i.get_text())
    
    news_data.append({"headline":title,"content": content, "timestamp": timestamp})
    return news_data

def getall_data(urls):
    news_data = []
    for url in urls:
        news_data.append(news_scraper(url))
    return news_data