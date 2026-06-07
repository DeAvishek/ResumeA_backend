from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
def BertSys(resume,job_desc):
    
    # Load tokenizer & model
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')

    # Tokenization
    inputs1 = tokenizer(resume, return_tensors="pt", truncation=True, padding=True)
    inputs2 = tokenizer(job_desc, return_tensors="pt", truncation=True, padding=True)

    # Generate embeddings
    with torch.no_grad():
        outputs1 = model(**inputs1)
        outputs2 = model(**inputs2)

    # Use [CLS] token embedding
    emb1 = outputs1.last_hidden_state[:, 0, :]
    emb2 = outputs2.last_hidden_state[:, 0, :]

    # Cosine similarity
    similarity_score = cosine_similarity(emb1.numpy(), emb2.numpy())[0][0]
    return similarity_score