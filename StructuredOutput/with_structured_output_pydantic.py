from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini", max_tokens = 500)

class Review(TypedDict):
    key_themes: list[str] = Field(description='A list of key themes or topics discussed in the review.')
    summary: str = Field(description='A brief summary of the review.')
    sentiment: Literal['pos', 'neg', 'neu'] = Field(description='The sentiment of the review, either positive, negative or neutral.')
    pros: Optional[list[str]] = Field(default=None, description='A list of pros mentioned in the review.')
    cons: Optional[list[str]] = Field(default=None, description='A list of cons mentioned in the review.')
    name: Optional[str] = Field(default=None, description='The name of the person who has reviewed.')

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
The iPhone 16 stands out as a reliable daily driver in 2026, powered by the efficient A18 chip and enhanced by the intuitive Camera Control button for quick, professional-grade shots. While the 60Hz display feels slightly dated compared to newer competitors, the device compensates with exceptional battery life that easily lasts a full day and a vibrant OLED screen that remains sharp and colorful. 

Pros:

Powerful A18 chip ensures smooth performance for years.
Excellent battery life and fast MagSafe charging.
Versatile 48MP camera system with improved low-light capabilities.
Durable design with the new Camera Control button. 

Cons:

Standard 60Hz refresh rate lacks the smoothness of Pro models.
Base storage of 128GB fills up quickly with high-res media.
Charging speed is slower than many Android flagships. 

Reviewer: Alex Mercer, Senior Tech Editor
""")

print(result)