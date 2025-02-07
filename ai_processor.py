import os
import openai
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

# Set your OpenAI API Key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Create a new client instance

def summarize_article(article_text: str) -> str:
    """Generate a summary of the given article."""
    prompt = f"Summarize this article in a few concise paragraphs:\n\n{article_text}"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )
    
    return response.choices[0].message.content

def chat_with_article(article_text: str, user_question: str) -> str:
    """Chat with the article using OpenAI GPT."""
    chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)

    messages = [
        SystemMessage(content="You are an AI assistant that helps users understand an article."),
        HumanMessage(content=f"Here is the article:\n{article_text}\n\nUser question: {user_question}")
    ]

    response = chat_model(messages)
    return response.content
