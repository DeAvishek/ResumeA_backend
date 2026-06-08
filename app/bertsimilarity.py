from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def BertSys(resume, job_desc):

    emb1 = model.encode([resume])
    emb2 = model.encode([job_desc])

    similarity_score = cosine_similarity(
        emb1,
        emb2
    )[0][0]

    return similarity_score