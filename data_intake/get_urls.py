import requests
from bs4 import BeautifulSoup

def get_news_urls(url,news_data):
    """
    Function to scrape the news articles from the provided URL
    :param url: URL of the webpage to scrape
    :param news_data: List to store the extracted news data
    """
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
        return []
    
    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # The elements containing the news articles have the class 'clearfix'
    # Find all news articles based on the provided structure
    news_items = soup.find_all('li', class_='clearfix')

    # Loop through each news item and extract details
    for item in news_items:
        # Extract the <a> tag inside the <h2>
        link_tag = item.find('h2').find('a') if item.find('h2') else None
        if link_tag:
            title = link_tag.get_text(strip=True)  # Clean the title text
            link = link_tag['href']  # Extract the href attribute (link)

            # Append the extracted data to the list
            news_data.append({"title": title, "link": link})

    return news_data

def getall_links(base_url,no_of_days=1):
    """
    Function to get all the news URLs from the provided URL for the specified number of days by scraping multiple pages
    here we are scraping 3 pages per day(2 pages of news and 1 page of margin)
    :param base_url: URL of the webpage wich have all the articles to scrape
    :param no_of_days: Number of days to scrape the news articles
    """
    # List to store the extracted news data
    news_data = []
    
    # Loop through the pages
    for i in range(no_of_days*3):   # 3 pages per day
        
        # Generate the URL by replacing "page-1" with "page-{i+1}"
        url = base_url.replace("page-1", f"page-{i+1}")
        
        # Call the function to scrape the page
        news_data = get_news_urls(url, news_data)

    return news_data
