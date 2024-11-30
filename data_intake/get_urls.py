import requests
from bs4 import BeautifulSoup

def get_news_urls(url,news_data):
    # Send a GET request to the website
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
        return []
    
    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
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

def getall_links(base_url,n=1):
    news_data = []
    
    # Loop through the pages
    for i in range(n*5):  # Assuming there are 4 pages to scrape
        # Generate the URL by replacing "page-1" with "page-{i+1}"
        url = base_url.replace("page-1", f"page-{i+1}")
        
        # Call the function to scrape the page
        news_data = get_news_urls(url, news_data)

    return news_data
