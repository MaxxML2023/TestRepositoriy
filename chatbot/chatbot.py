from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
template = """
Here is history: {context}
Question: {question}
Answer:
"""
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to AI Chatbot, Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke(input={"question": user_input, "context": context})


        print(result)
handle_conversation()