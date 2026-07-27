from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2.5-7B-Instruct',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template='Give a detailed report on {topic}',
    input_variables=['topic']
)

prompt1 = template1.invoke({'topic':'Football'})

result1 = model.invoke(prompt1)

template2 = PromptTemplate(
    template='Give a 5 line summary on the following text:- \n {text}',
    input_variables=['text']
)

prompt2 = template2.invoke({'text': result1.content})

result2 = model.invoke(prompt2)

print(result2.text)