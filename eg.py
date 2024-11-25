from data_intake.get_urls import getall_links
from data_intake.web_crawler import getall_data
import pandas as pd

# URL for the news articles
url = "https://www.livemint.com/latest-news/page-1"
urls = getall_links(url)

urls = [item['link'] for item in urls]
#print(urls)

# Scrape the news articles
news_data = getall_data(urls)
print(news_data[5])