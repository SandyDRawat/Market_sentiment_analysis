from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import scipy
import pandas as pd

# Load FinBERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")


def finbert_sentiment(text: str):
    """
    Analyze sentiment using FinBERT.
    Args:
        text (str): The input text to analyze.
    Returns:
        dict: A dictionary with sentiment scores and the predicted label.
    """
    with torch.no_grad():
        # Tokenize input
        inputs = tokenizer(
            text, return_tensors="pt", padding=True, truncation=True, max_length=512
        )
        # Get model outputs
        outputs = model(**inputs)
        logits = outputs.logits
        # Calculate softmax probabilities
        scores = {
            k: v
            for k, v in zip(
                model.config.id2label.values(),
                scipy.special.softmax(logits.numpy().squeeze()),
            )
        }
        # Return scores and the predicted label
        return {
            "positive": scores["positive"],
            "negative": scores["negative"],
            "neutral": scores["neutral"],
            "predicted_label": max(scores, key=scores.get),
        }
    
def add_sentiment_to_data(data):
    """
    Add sentiment analysis results to the given data.
    Args:
        data (pd.DataFrame): The input data with a 'content' column.
    Returns:
        pd.DataFrame: The data with sentiment analysis results added.
    """
    
    data[['positive', 'negative', 'neutral', 'predicted_label']] = data['content'].apply(finbert_sentiment).apply(pd.Series)
    data["Score"] = data["positive"] - data["negative"]
    return data

if __name__ == '__main__':
    data = pd.read_csv('D:/projects/Market sentiment analysis/articles_with_summary.csv')
    data[['positive', 'negative', 'neutral', 'predicted_label']] = data['content'].apply(finbert_sentiment).apply(pd.Series)
    data["Score"] = data["positive"] - data["negative"]
    print(data.head(5))
    data.to_csv('D:/projects/Market sentiment analysis/articles_with_sentiment.csv', index=False)