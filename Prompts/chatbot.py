from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4o-mini')

chat_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    chat_history.append({"role": "user", "content": user_input})
    response = model.invoke(chat_history)
    chat_history.append({"role": "assistant", "content": response.content})
    print(f"Assistant: {response.content}")

print(chat_history)
