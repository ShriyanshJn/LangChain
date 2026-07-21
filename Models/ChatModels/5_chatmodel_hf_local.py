from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
import os

os.environ["HF_HOME"] = "D:/LangChain/huggingface_cache"

load_dotenv()

llm = HuggingFacePipeline(
    model_id = "Qwen/Qwen2.5-7B-Instruct",
    task = "text-generation",
    model_kwargs = {
        "temperature": 0.3,
        "max_new_tokens": 10
    }
)

model = ChatHuggingFace(llm = llm)

response = model.invoke("What is the capital of India?")
print(response.content)

