from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage ,HumanMessage,SystemMessage

model=ChatMistralAI(model="mistral-small-2506")

user=int(input("Choice the number(1 for angry mode , 2 for joyful mode , 3 for sad mode): "))
match user:
 case 1:
    mode="You are an angry AI agent. You respond aggressively and impatiently"
 case 2:
    mode=   "You are an enjoyful AI agent. You respond joyful and enjoyful"    
 case 3:
    mode=  "You are an sad AI agent. You respond sadly and painful"
 case _:
    print("enter valid number : ")        
print("to exit press 0")
messages=[
   SystemMessage(content=mode)
]        


while True:
    prompt=input("me: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break 
    response=model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("AI: ",response.content)
print(messages)    