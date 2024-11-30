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

---
### 2. Install Dependencies
Install the required Python libraries:

```bash
pip install -r requirements.txt

---