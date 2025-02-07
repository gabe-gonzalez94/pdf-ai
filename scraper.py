import requests
from bs4 import BeautifulSoup

def extract_article_text(url: str) -> str:
    """Fetch and extract main content from a webpage."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")

        article_text = "\n".join([p.get_text() for p in paragraphs])
        return article_text if article_text else "Could not extract content."
    
    except requests.RequestException as e:
        return f"Error fetching article: {str(e)}"