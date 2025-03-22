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

# print(llm.invoke("What is the capital of India?"))

# The agent state is the input to each node in the graph
class AgentState(MessagedState):
    # The next field indicates where to route to next
    next: str

# Member agent names
members = []


# Node :- Supervisor LLM Node -> \
# Picks up the next agent to process and \
# decides when the work is completed
options = members + ["FINISH"]

system_prompt = (
    f"""You are a supervisor tasked with managing \
        a conversation between the following workers: \
        {members}. Given the following user request, \
        respond with the worker to act next. """
)

class SupervisorState(TypedDict):
    """Worker to route to next. If no wokers needed\
        route to finish"""
    next: Literal[*options]

    







































































