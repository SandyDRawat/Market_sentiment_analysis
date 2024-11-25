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
    
    for headline in soup.find_all('h2', class_='headline'):
        # Extract the <a> tag inside the <h2>
        link_tag = headline.find('a')
        if link_tag:
            title = link_tag.get_text(strip=True)  # Clean the title text
            link = link_tag['href']  # Extract the href attribute (link)
            
            # Complete the link if it's relative
            if not link.startswith("http"):
                link = "https://www.livemint.com/latest-news" + link
            
            news_data.append({"title": title, "link": link})
    
    return news_data

def getall_links(base_url):
    news_data = []
    
    # Loop through the pages
    for i in range(4):  # Assuming there are 4 pages to scrape
        # Generate the URL by replacing "page-1" with "page-{i+1}"
        url = base_url.replace("page-1", f"page-{i+1}")
        
        # Call the function to scrape the page
        news_data = get_news_urls(url, news_data)

    return news_data
