# Market Sentiment Analysis

This project analyzes market sentiment by scraping news articles from [Moneycontrol](https://www.moneycontrol.com), summarizing the content, and performing sentiment analysis to extract meaningful insights. The processed data includes sentiment scores and summaries, which can be saved for further analysis.

---

## Features

- **Web Scraping**: Collects market news articles for a specified number of days.
- **Summarization**: Summarizes the content of news articles using an LLM.
- **Sentiment Analysis**: Analyzes the sentiment (positive, negative, neutral) of the articles using FinBERT.
- **Data Export**: Optionally saves the processed data with summaries and sentiment scores to a CSV file.

---

## Table of Contents

1. [Setup](#setup)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Dependencies](#dependencies)
5. [Example Output](#example-output)
6. [License](#license)

---

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/market-sentiment-analysis.git
cd market-sentiment-analysis
```
### 2. Install Dependencies
Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 3. COnfigure API Keys
Store your API keys(Hugging Face) in .env file:

```plaintext
HUGGINGFACE_API_KEY=your_huggingface_api_key
```
---

## Usage

### 1. Run the streamlit App
Launch the streamlit interface to analyze sentiment interactively:

```bash
streamlit run app.py
```
### 2. Use the ```get_data``` Function
To scrape, summarize, and analyze sentiment programmatically:

```python
from your_project_module import get_data

# Fetch and process articles for the last 3 days
data = get_data(no_of_days=3, download_csv=True)
```
---

### Project Structure
```plaintext
.
├── data_intake/
│   ├── get_urls.py          # Fetches article URLs
│   ├── web_crawler.py       # Scrapes article content
├── data_preprocess/
│   ├── add_summary.py       # Adds summaries to articles
│   ├── add_sentiment.py     # Adds sentiment analysis
├── app.py                   # Streamlit application
├── main.py                  # Main script for fetching and processing data
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
└── .env                     # Environment variables (not tracked in Git)

```
---