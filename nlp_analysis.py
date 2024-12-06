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
        print(user_embedding)
        article_embeddings = model.encode(articles, convert_to_tensor=True)
        print(article_embeddings)

        # Compute cosine similarity scores
        scores = util.pytorch_cos_sim(user_embedding, article_embeddings)
        print(scores)

        # Convert scores to a list for easier processing
        return scores[0].tolist()
    except Exception as e:
        print(f"Error in calculating similarity: {e}")
        return []

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




# def classify_fake_news(similarity_scores, threshold=0.5):
#     """
#     Classifies the news as Real or Fake based on similarity scores.

#     Args:
#         similarity_scores (list): Cosine similarity scores between user text and articles.
#         threshold (float): The threshold value to classify as Real or Fake.

#     Returns:
#         str: Classification result ("Real" or "Fake").
#     """
#     if not similarity_scores:
#         return "Unable to classify due to missing or invalid similarity scores."

#     # Debugging: Print similarity scores
#     print("Similarity Scores:", similarity_scores)

#     # Count the number of scores above the threshold
#     scores_above_threshold = [score for score in similarity_scores if score >= threshold]

#     # Calculate the percentage of scores above the threshold
#     # percentage_above_threshold = (len(scores_above_threshold) / len(similarity_scores)) * 100

#     # Debugging: Print percentage above the threshold
#     # print(f"Percentage of scores above threshold ({threshold}): {percentage_above_threshold}%")

#     # Classify as Real or Fake based on the percentage above the threshold
#     if scores_above_threshold >= 75:  # At least 75% of scores should be above the threshold
#         return "Real"
#     else:
#         return "Fake"
