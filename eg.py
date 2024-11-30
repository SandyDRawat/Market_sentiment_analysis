from data_preprocess.add_sentiment import add_sentiment_to_data
import pandas as pd
from data_preprocess.add_sentiment import add_sentiment_to_data

from data_intake.data_intake import get_data
print("fgjghkjjnntynynynynynynynh",type(pd.read_csv('D:/projects/Market sentiment analysis/articles_with_summary.csv')))
data = get_data(1)
for i in range(len(data)):
    data['content'][i] = str(data['content'][i])
data = add_sentiment_to_data(data)
print(data.head(5))