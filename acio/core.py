from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

from langchain_mistralai import ChatMistralAI

model=ChatMistralAI(model="mistral-small-2506")

prompt=ChatPromptTemplate.from_messages([("system","""You are a professional summarizer who gives structured and precise outputs.
"""),("human","""Summarize the paragraph below.
Instructions:
- 1 sentence for main idea
- 2-3 bullet points for key details
- Keep it short and factual
Paragraph:
{paragraph}
Output format:
Main Idea:
- ...
Key Points:
- ...
- ...
- ...
""")])

para=input("give me paragraph")

final=prompt.invoke(
    {"paragraph":para}
)

response=model.invoke(final)
print(response.content)