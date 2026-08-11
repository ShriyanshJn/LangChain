from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template = 'Write pros on the topic of {topic}.',
    input_variables = ['topic'],
)

prompt2 = PromptTemplate(
    template = 'Write cons on the topic of {topic}.',
    input_variables = ['topic'],
)

parser = StrOutputParser()

chain = RunnableParallel({
    "pros": RunnableSequence(prompt1,model,parser),
    "cons": RunnableSequence(prompt2,model,parser)
})

result = chain.invoke({'topic':'programming'})
print(result["pros"])
print(result["cons"])