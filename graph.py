import os
from dotenv import load_dotenv
from typing import TypedDict, Literal
from langgraph.graph import MessagesState,StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI

load_dotenv(r"../aiwork.env")

MAX_TOKENS = 500

# Create the LLM
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0, 
    max_tokens=MAX_TOKENS,
    max_retries=2,
    timeout=None
    )

print(llm.invoke("What is the capital of India?"))





