import requests
from bs4 import BeautifulSoup

def news_scraper(url):
    """
    function to scrape data form the news article page like content, description, timestamp
    :param url: URL of the news article page
    """
    # List to store the extracted data
    news_data = []
    content = []

    # set description to "Description not found" by default if found it will be updated
    description = "Description not found"
    #print(url)

    # Fetch the webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div with id 'contentdata'
    content_div = soup.find('div', id='contentdata')
    # Find the div with class 'slideshow-caption article_text' for the articles with multiple slides(stocks) eg. top 10 movers
    slideshow_content = soup.find_all('span',class_ = "slideshow-caption article_text")
    # Find the div with class 'article_desc' for the description
    description_element = soup.find('h2', class_='article_desc')
    

    if description_element:
    # Extract and clean the description text if aviailable
        description = description_element.get_text(strip=True)
        #print("Description:", description)

    # If the div is found, extract text from all 'p' tags inside it
    if content_div:
        paragraphs = content_div.find_all('p')
        for p in paragraphs:
            text = p.get_text(strip=True)            # Extract and clean the text
            content.append(text)                     # Append to the list
    elif slideshow_content:                          #same for the articles with multiple slides
        for p in slideshow_content:
            text = p.get_text(strip=True)
            content.append(text)
    else:
        print("Coudn't find the content")
        return 'Nan'

    # Extract the timestamp
    timestamp = soup.find('div',class_ = 'tags_last_line')
    if timestamp:
        timestamp = timestamp.get_text().split(': ')[1]
    else:
        timestamp = "Timestamp not found"
    
    # Extract the title
    title =  "Title not found"
    h1_tag = soup.find('h1', class_='article_title artTitle')
    if h1_tag:
        title = h1_tag.get_text()

    # Store the extracted data in a dictionary
    news_data = {"headline":title ,"description":description, "content": str(content), "timestamp": timestamp}
    return news_data

def getall_data(urls):
    """
    Function to scrape data from all the news article URLs
    :param urls: List of URLs to scrape
    """
    news_data = []
    for url in urls:                                       # Loop through the URLs                     
        news_data.append(news_scraper(url))                # Store the dict output of news_scraper in the list
    return news_data