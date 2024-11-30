import requests
from bs4 import BeautifulSoup

def news_scraper(url):
    news_data = []
    content = []
    description = "Description not found"
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

        # Find the div with id 'contentdata'
    content_div = soup.find('div', id='contentdata')
    slideshow_content = soup.find_all('span',class_ = "slideshow-caption article_text")
    description_element = soup.find('h2', class_='article_desc')
    

    if description_element:
    # Extract and clean the description text
        description = description_element.get_text(strip=True)
        #print("Description:", description)

    # If the div is found, extract text from all 'p' tags inside it
    if content_div:
        paragraphs = content_div.find_all('p')
        for p in paragraphs:
            text = p.get_text(strip=True)  # Extract and clean the text
            content.append(text)  # Or do something else with the extracted text
    elif slideshow_content:
        for p in slideshow_content:
            text = p.get_text(strip=True)
            content.append(text)
    else:
        print("Div with id 'contentdata' not found.")
        return 'Nan'


    timestamp = soup.find('div',class_ = 'tags_last_line')
    if timestamp:
        timestamp = timestamp.get_text().split(': ')[1]
    else:
        timestamp = "Timestamp not found"
    title =  "Title not found"
    h1_tag = soup.find('h1', class_='article_title artTitle')
    if h1_tag:
        title = h1_tag.get_text()

    
    news_data = {"headline":title ,"description":description, "content": str(content), "timestamp": timestamp}
    return news_data

def getall_data(urls):
    news_data = []
    for url in urls:
        news_data.append(news_scraper(url))
    return news_data