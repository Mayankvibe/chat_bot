from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage ,HumanMessage,SystemMessage

model=ChatMistralAI(model="mistral-small-2506",temperature=0.9)
messages=[
    SystemMessage("You are an angry AI agent. You respond aggressively and impatiently")
]
print("to exit press 1")
while True:
    prompt=input("me: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "1":
        break 
    response=model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("AI: ",response.content)
print(messages)    