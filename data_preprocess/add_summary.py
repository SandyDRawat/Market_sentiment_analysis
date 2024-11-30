from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
import pandas as pd
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Using Falcon-7B-Instruct, a large language model for generating text
llm = HuggingFaceHub(
    repo_id="tiiuae/falcon-7b-instruct",                          # The model repository ID on Hugging Face Hub
    model_kwargs={"temperature": 0.5},                            # Setting the temperature for response diversity
    huggingfacehub_api_token = os.getenv("HUGGINGFACE_API_KEY"),  # API token for authentication
)

def add_summary(article):
    """
    Generate a summary for a given news article using an LLM.
    Args:
        article (str): The content of a news article.
    Returns:
        str: The summarized text of the article.
    """
    # Define a prompt template for summarization
    prompt_template_summary = PromptTemplate(
        input_variables=["content"],  # Variable to be replaced in the template
        template="""Summarize the following news content in a few sentences.

        News Content: {content}

        Summary:"""  # Prompt structure to guide the LLM
    )
    
    # Create a chain to process the prompt and generate a response
    Summary_chain = LLMChain(
    llm=llm,                            # Language model to be used
    prompt=prompt_template_summary      # Template for the summarization task
    )
    
    # Invoke the chain to get the response
    response = Summary_chain.invoke({"content": article})
    
    # Extract the generated summary from the response
    return response['text'].split('Summary:')[-1]

def add_summary_to_data(data):
    """
    Add summaries to each article in the dataset.
    Args:
        data (pd.DataFrame): A DataFrame containing a 'content' column 
                             with news articles.
    Returns:
        pd.DataFrame: The original DataFrame with an additional 'summary' 
                      column containing the summaries of each article.
    """
    # Apply the summarization function to each article in the 'content' column
    data['summary'] = data['content'].apply(add_summary)
    return data


if __name__ == '__main__':
    data = pd.read_csv('D:/projects/Market sentiment analysis/articles.csv')
    data_with_summary = add_summary_to_data(data)
    print(data_with_summary)
    data_with_summary.to_csv('D:/projects/Market sentiment analysis/articles_with_summary.csv', index=False)
