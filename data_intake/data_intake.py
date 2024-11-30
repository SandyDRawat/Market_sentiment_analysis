from data_intake.get_urls import getall_links
from data_intake.web_crawler import getall_data
from data_preprocess.add_summary import add_summary_to_data
from data_preprocess.add_sentiment import add_sentiment_to_data
import pandas as pd

# URL for the news articles
url = "https://www.moneycontrol.com/news/business/markets/page-1/"

def get_data(no_of_days,download_csv=False):
    """
    Function to get the news articles, summarize them and add sentiment to them
    :param no_of_days: Number of days to scrape the news articles"""

    # Use getall_links to get all the links of the news articles
    urls = getall_links(url,no_of_days)

    # Extract the links from the dictionary
    urls = [item['link'] for item in urls]
    #print(urls)

    # Filter the URLs to get only the market news articles
    filtered_urls = [i for i in urls if i.startswith('https://www.moneycontrol.com/news/business/markets/')]

    # Scrape the news articles
    news_data = getall_data(filtered_urls)
    #print(type(news_data))

    # Remove all non-dict entries from the list
    news_data = [item for item in news_data if isinstance(item, dict)]
    # Convert the list of dictionaries to a DataFrame
    news_data = pd.DataFrame(news_data)

    # Add summary column to the news articles data
    news_data = add_summary_to_data(news_data)
    
    # Add sentiment columns to the news articles data
    news_data = add_sentiment_to_data(news_data)
    
    # Save the data to a csv file if download_csv is True
    if download_csv:
        news_data.to_csv('D:/projects/Market sentiment analysis/articles_with_summary_and_sentiment.csv', index=False)

    return news_data