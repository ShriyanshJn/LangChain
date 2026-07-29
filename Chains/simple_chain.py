from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Give top 5 most streamed tracks of the artist: {artist}',
    input_variables=['artist']
)

parser = StrOutputParser()

model = ChatOpenAI()

chain = prompt | model | parser

result = chain.invoke({'artist' : 'Tory Lanez'})

print(result)

chain.get_graph().print_ascii()