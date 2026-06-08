import math
def getFinalScore(
    tf_idf_similarity_score,
    sentiment_compound,
    skill_score
):

    weight_configs = {
        "skill": 0.60,
        "tfidf": 0.30,
        "sentiment": 0.10
    }

    final_score = (
        weight_configs["skill"] * skill_score +
        weight_configs["tfidf"] * tf_idf_similarity_score +
        weight_configs["sentiment"] * sentiment_compound
    )

    return math.ceil(final_score * 100)