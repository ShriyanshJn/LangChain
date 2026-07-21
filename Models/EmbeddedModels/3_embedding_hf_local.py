from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

docs = [
    "Delhi is the capital of India.",
    "Mumbai is the financial capital of India.",
    "Bangalore is the tech hub of India."
]

vector = embedding.embed_documents(docs)
print(str(vector))
