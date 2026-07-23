from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate   

load_dotenv()

st.header('Research Tool')
st.write('Please select as required.')

col1, col2, col3 = st.columns(3)

research_paper = col1.selectbox('Research Paper', ['Attention Is All You Need', 'ImageNet Classification with Deep Convolutional Neural Networks', 'Deep Residual Learning for Image Recognition', 'Language Models are Few-Shot Learners'])

research_style = col2.selectbox('Research Style', ['Formal', 'Informal', 'Technical', 'Layman'])

research_length = col3.selectbox('Research Length', ['Small', 'Medium', 'Long'])

model = ChatOpenAI(model = 'gpt-3.5-turbo')

template = PromptTemplate(
    template = """You are a research assistant. 
    Please summarize the research paper '{research_paper}' in a '{research_style}' style and '{research_length}' length.
    1. Mathematical Details:
        Include relevant mathematical equations, formulas, and derivations if present in the paper.
        Explain the mathematical concepts using simple, intuitive code snippets where applicable.
    2. Analogies:
        Use relatable analogies to simplify complex ideas and make them more understandable.
    If certain information is not available in the paper, respond with 'Insufficient information available' instead of guesssing.
    Ensure that the summary is clear, accurate and aligned with provided style and length requirements.
    """,
    input_variables = ['research_paper', 'research_style', 'research_length'],
    validate_template = True)

prompt = template.invoke({
    'research_paper': research_paper,
    'research_style': research_style,
    'research_length': research_length
})

if(st.button('Generate Summary')):
    with st.spinner('Generating summary...'):
        response = model.invoke(prompt,max_tokens=500)
        st.subheader('Summary:')
        st.write(response.content)
