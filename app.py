from flask import Flask, request, render_template
from scrapper import scrape_articles, extract_article_content
from nlp_analysis import calculate_similarity, classify_fake_news
from storage import save_result

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user input
        user_text = request.form["news_input"]
        
        # Scrape articles
        articles_urls = scrape_articles(user_text)
        articles_content = [extract_article_content(url) for url in articles_urls]
        
        # Perform NLP analysis
        similarity_scores = (calculate_similarity(user_text, articles_content))
        classification = classify_fake_news(similarity_scores)
        
        # Save results
        save_result(user_text, classification, articles_urls)
        
        # Return results
        return render_template("index.html", result=classification, articles=articles_urls)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
