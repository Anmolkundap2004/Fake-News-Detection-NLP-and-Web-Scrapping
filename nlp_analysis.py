from sentence_transformers import SentenceTransformer, util

# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def calculate_similarity(user_text, articles):
    """
    Calculates similarity scores between user input and a list of scraped articles.

    Args:
        user_text (str): The input news text provided by the user.
        articles (list): A list of article texts from trusted websites.

    Returns:
        list: Similarity scores between user text and each article.
    """
    try:
        # Encode user input and articles into embeddings
        user_embedding = model.encode(user_text, convert_to_tensor=True)
        article_embeddings = model.encode(articles, convert_to_tensor=True)

        # Compute cosine similarity scores
        scores = util.pytorch_cos_sim(user_embedding, article_embeddings)

        # Convert scores to a list for easier processing
        return scores[0].tolist()
    except Exception as e:
        print(f"Error in calculating similarity: {e}")
        return []

'''
def classify_fake_news(similarity_scores, threshold=0.6):
    """
    Classifies the news as Real or Fake based on similarity scores.

    Args:
        similarity_scores (list): Cosine similarity scores between user text and articles.
        threshold (float): The threshold value to classify as Real or Fake.

    Returns:
        str: Classification result ("Real" or "Fake").
    """
    if not similarity_scores:
        return "Unable to classify due to missing or invalid similarity scores."

    # Calculate the average similarity score
    avg_similarity = sum(similarity_scores) / len(similarity_scores)

    # Classify as Real or Fake based on the threshold
    if avg_similarity >= threshold:
        return "Real"
    else:
        return "Fake"
'''


def classify_fake_news(similarity_scores, threshold=0.5):
    """
    Classifies the news as Real or Fake based on similarity scores.

    Args:
        similarity_scores (list): Cosine similarity scores between user text and articles.
        threshold (float): The threshold value to classify as Real or Fake.

    Returns:
        str: Classification result ("Real" or "Fake").
    """
    if not similarity_scores:
        return "Unable to classify due to missing or invalid similarity scores."

    # Debugging: Print similarity scores
    print("Similarity Scores:", similarity_scores)

    # Calculate the average similarity score
    avg_similarity =(sum(similarity_scores) / len(similarity_scores))*10

    # Debugging: Print the average similarity
    print("Average Similarity:", avg_similarity)

    # Classify as Real or Fake based on the threshold
    if avg_similarity >= threshold:
        return "Real"
    else:
        return "Fake"


