from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scraper import extract_article_text
from ai_processor import summarize_article, chat_with_article

app = FastAPI()

class ArticleRequest(BaseModel):
    url: str

class ChatRequest(BaseModel):
    url: str
    question: str

@app.get("/")
def read_root():
    return {"message": "AI Article Analyzer API is running!"}

@app.post("/summarize/")
def summarize_article_endpoint(request: ArticleRequest):
    """Fetch an article and summarize its content."""
    article_text = extract_article_text(request.url)
    if "Error" in article_text:
        raise HTTPException(status_code=400, detail=article_text)
    
    summary = summarize_article(article_text)
    return {"summary": summary}

@app.post("/chat/")
def chat_with_article_endpoint(request: ChatRequest):
    """Allow users to chat with an article."""
    article_text = extract_article_text(request.url)
    if "Error" in article_text:
        raise HTTPException(status_code=400, detail=article_text)
    
    response = chat_with_article(article_text, request.question)
    return {"response": response}
