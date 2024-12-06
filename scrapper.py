import requests
from newspaper import Article
from bs4 import BeautifulSoup

def scrape_articles(query, num_results=10):
    """
    Fetch search results using the Google Custom Search API (replace this with API integration).
    
    Args:
    - query (str): The search query.
    - num_results (int): Number of results to fetch.

    Returns:
    - urls (list): A list of URLs from search results.
    """
    # Placeholder: Replace with Google Custom Search JSON API
    query = query.replace(" ", "+")
    # News domains to scrape from
    domains = [
        "bbc.com", "cnn.com", "nytimes.com", "reuters.com", 
        "foxnews.com", "theguardian.com", "washingtonpost.com", 
        "forbes.com", "aljazeera.com", "bloomberg.com", "news18.com"
    ]
    urls = []

    headers = {"User-Agent": "Mozilla/5.0"}
    for domain in domains:
        try:
            search_url = f"https://www.google.com/search?q={query}+site:{domain}"
            response = requests.get(search_url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            
            for link in soup.find_all("a", href=True):
                href = link['href']
                if domain in href:
                    clean_link = href.split("&")[0].replace("/url?q=", "")
                    urls.append(clean_link)
                    if len(urls) >= num_results:
                        break
            if len(urls) >= num_results:
                break
        except Exception as e:
            print(f"Error with domain {domain}: {e}")
    return urls



def extract_article_content(url):
    """
    Extracts the main content of a news article.
    
    Args:
    - url (str): The URL of the article.
    
    Returns:
    - content (str): The main text of the article.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()
        
        return article.text
    except Exception as e:
        print(f"Error extracting content from {url}: {e}")
        return ""

