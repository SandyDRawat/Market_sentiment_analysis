from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import scipy
import pandas as pd

# Load the FinBERT model and tokenizer
# FinBERT is specifically trained for financial sentiment analysis.
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")


def finbert_sentiment(text: str):
    """
    Analyze sentiment using FinBERT.
    
    Args:
        text (str): The input text (financial news/article) to analyze.
    
    Returns:
        dict: A dictionary containing sentiment scores for 'positive',
              'negative', 'neutral', and the predicted label with the
              highest score.
    """
    with torch.no_grad():  # Disables gradient calculation to save memory and improve performance
        # Tokenize the input text for FinBERT
        inputs = tokenizer(
            text, 
            return_tensors="pt",  # Return PyTorch tensors
            padding=True,         # Add padding to match input sizes
            truncation=True,      # Truncate inputs longer than the max length
            max_length=512        # Maximum sequence length supported by FinBERT
        )
        
        # Get the logits (raw scores) from the model
        outputs = model(**inputs)
        logits = outputs.logits
        
        # Apply softmax to convert logits to probabilities
        scores = {
            k: v
            for k, v in zip(
                model.config.id2label.values(),  # Map label IDs to label names
                scipy.special.softmax(logits.numpy().squeeze()),  # Convert logits to probabilities
            )
        }
        
        # Return a dictionary with scores and the predicted sentiment label
        return {
            "positive": scores["positive"],
            "negative": scores["negative"],
            "neutral": scores["neutral"],
            "predicted_label": max(scores, key=scores.get),  # Label with the highest probability
        }

def add_sentiment_to_data(data):
    """
    Add sentiment analysis results to the given data.
    
    Args:
        data (pd.DataFrame): The input data with a 'content' column
                             containing financial text/articles.
    
    Returns:
        pd.DataFrame: The original DataFrame with additional columns for 
                      sentiment scores ('positive', 'negative', 'neutral'), 
                      the predicted label, and a sentiment score difference.
    """
    
    # Apply the sentiment analysis function to the 'content' column
    # and expand the resulting dictionary into separate columns
    data[['positive', 'negative', 'neutral', 'predicted_label']] = (
        data['content'].apply(finbert_sentiment).apply(pd.Series)        
        # Apply sentiment analysis to each article and convert the dictionary output to columns
    )
    # Calculate a sentiment score by subtracting the negative score from the positive score
    data["Score"] = data["positive"] - data["negative"]
    return data

if __name__ == '__main__':
    data = pd.read_csv('D:/projects/Market sentiment analysis/articles_with_summary.csv')

    data[['positive', 'negative', 'neutral', 'predicted_label']] = (data['content'].apply(finbert_sentiment).apply(pd.Series))

    data["Score"] = data["positive"] - data["negative"]
    print(data.head(5))
    data.to_csv('D:/projects/Market sentiment analysis/articles_with_sentiment.csv', index=False)
