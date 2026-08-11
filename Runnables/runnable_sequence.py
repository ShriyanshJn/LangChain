from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template = 'Write a joke on the topic of {topic}.',
    input_variables = ['topic'],
)

prompt2 = PromptTemplate(
    template = 'Summarize the following joke: {joke}',
    input_variables = ['joke'],
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,prompt2,model,parser)

result = chain.invoke({'topic':'programming'})

print(result)