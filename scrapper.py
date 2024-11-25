import requests
from bs4 import BeautifulSoup

def scrape_articles(query, num_articles=3):
    """
    Scrapes related news articles from Google News.
    """
    query = query.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}+site:reuters.com"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    for link in soup.find_all("a", href=True):
        href = link['href']
        if "reuters.com" in href:
            full_link = href.split("&")[0]
            articles.append(full_link.replace("/url?q=", ""))
            if len(articles) >= num_articles:
                break
    
    return articles

def extract_article_content(url):
    """
    Extracts article content from a given URL.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all('p')
        content = " ".join([p.get_text() for p in paragraphs])
        return content
    except Exception as e:
        return ""
