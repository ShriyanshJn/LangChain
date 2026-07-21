from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import time

start = time.time()
load_dotenv()
print("dotenv:", time.time() - start)

start = time.time()
embedding = OpenAIEmbeddings(model = 'text-embedding-3-small')
print("Create object:", time.time() - start)

documents = [
    "Virat Kohli is one of India's most successful batters.",
    "Rohit Sharma is known for his elegant stroke play and captaincy.",
    "Jasprit Bumrah is famous for his unique bowling action and deadly yorkers.",
    "MS Dhoni is celebrated for his calm leadership and exceptional finishing skills.",
    "Sachin Tendulkar is regarded as one of the greatest cricketers in history."
]

query = "Tell me about Bumrah."

start = time.time()
document_embeddings = embedding.embed_documents(documents)
print("Documents:", time.time() - start)

start = time.time()
query_embedding = embedding.embed_query(query)
print("Query:", time.time() - start)

start = time.time()
scores = cosine_similarity([query_embedding], document_embeddings)[0]
print("Similarity:", time.time() - start)

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(query)
print(documents[index])

print(f"Similarity Score: {score}")