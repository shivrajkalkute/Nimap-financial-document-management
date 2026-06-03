import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
collection = client.get_or_create_collection('documents')
model = SentenceTransformer('all-MiniLM-L6-v2')

def index_document(doc_id,text):
    emb=model.encode(text).tolist()
    collection.add(ids=[str(doc_id)],embeddings=[emb],documents=[text])

def search(query):
    emb=model.encode(query).tolist()
    return collection.query(query_embeddings=[emb],n_results=5)
