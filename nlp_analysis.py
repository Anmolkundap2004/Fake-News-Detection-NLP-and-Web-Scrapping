from sentence_transformers import SentenceTransformer, util

# Load the pre-trained model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def calculate_similarity(user_text, articles):
    """
    Calculates similarity scores between user input and scraped articles.
    """
    user_embedding = model.encode(user_text)
    article_embeddings = model.encode(articles)
    
    scores = util.pytorch_cos_sim(user_embedding, article_embeddings)
    return scores.tolist()

def classify_fake_news(similarity_scores, threshold=0.6):
    """
    Classifies the input as fake or real based on similarity scores.
    """
    if max(similarity_scores) >= threshold:
        return "Real"
    else:
        return "Fake"
