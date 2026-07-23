from langchain_core.prompts import PromptTemplate

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

template.save('Prompts/template.json')