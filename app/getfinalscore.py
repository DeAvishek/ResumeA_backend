import math
def getFinalScore(BertSimilarityScore,tf_idf_similarity_score,sentiment_compund,skill_score):
    weight_configs = {
            "skill": 0.50,    # Skills are most important
            "tfidf": 0.20,    # Keyword matching
            "bert": 0.20,     # Semantic understanding
            "sentiment": 0.10  # Tone matters less
    }
    final_score = (weight_configs["skill"]*skill_score+
                  weight_configs["tfidf"]*tf_idf_similarity_score+
                  weight_configs["bert"]*BertSimilarityScore+
                  weight_configs["sentiment"]*sentiment_compund)
    return math.ceil(final_score*100)