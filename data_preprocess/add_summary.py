from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
import pandas as pd

llm = HuggingFaceHub(
    repo_id="tiiuae/falcon-7b-instruct",
    model_kwargs={"temperature": 0.5},
    huggingfacehub_api_token="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",
    
)

def add_summary(article):
    prompt_template_summary = PromptTemplate(
        input_variables=["content"],
        template="""Summarize the following news content in a few sentences.

        News Content: {content}

        Summary:"""
    )
    Summary_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_summary
    )

    response = Summary_chain.invoke({"content": article}) 
    return response['text'].split('Summary:')[-1]

def add_summary_to_data(data):
    data['summary'] = data['content'].apply(add_summary)
    return data


if __name__ == '__main__':
    data = pd.read_csv('D:/projects/Market sentiment analysis/articles.csv')
    data_with_summary = add_summary_to_data(data)
    print(data_with_summary)
    data_with_summary.to_csv('D:/projects/Market sentiment analysis/articles_with_summary.csv', index=False)