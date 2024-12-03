from sentence_transformers import SentenceTransformer, util

# Load the pre-trained model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def calculate_similarity(user_text, articles):
    """
    Calculates similarity scores between user input and scraped articles.
    """
    # Encode user input and articles
    user_embedding = model.encode(user_text, convert_to_tensor=True)
    article_embeddings = model.encode(articles, convert_to_tensor=True)
    
    # Calculate cosine similarity
    scores = util.pytorch_cos_sim(user_embedding, article_embeddings)
    
    # Convert scores to a 1D list
    similarity_scores = scores.squeeze(0).tolist()
    return similarity_scores


def classify_fake_news(similarity_scores, threshold=0.6):
    """
    Classifies the input as fake or real based on similarity scores.
    """
    # Calculate the average similarity score
    average_score = sum(similarity_scores) / len(similarity_scores)
    
    # Compare the average score with the threshold
    if average_score >= threshold:
        return "Real"
    else:
        return "Fake"
