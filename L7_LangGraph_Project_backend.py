# Model calling and intial setup
import os
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
import warnings
warnings.filterwarnings("ignore") 

load_dotenv()
# Load env
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
AZURE_BASE_URL = os.getenv("AZURE_BASE_URL")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_CHAT_DEPLIOYMENT_NAME = os.getenv("AZURE_CHAT_DEPLIOYMENT_NAME")

parser = StrOutputParser()

# llm_gemini = ChatGoogleGenerativeAI(model="gemini-2.0-flash" , api_key= GOOGLE_API_KEY)

llm_openai = AzureChatOpenAI(
    model="gpt-4o-mini",                         
    deployment_name=AZURE_CHAT_DEPLIOYMENT_NAME ,  # deployment name in Azure
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_BASE_URL,
    api_version="2024-02-01"
) 

# ChatBot workflow
from langgraph.graph import StateGraph , START , END
from typing import TypedDict , Annotated
import operator
from langchain_core.messages import BaseMessage , HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver


class ChatState(TypedDict):
    msg : Annotated[list[BaseMessage] , add_messages]
    
def chat(state:ChatState)->ChatState:
    chat_chain = llm_openai | parser
    
    ai_msg = chat_chain.invoke(state['msg'])
    return {"msg" : [ai_msg]}

# create graph
graph = StateGraph(ChatState)

# creating checkpointer
checkpointer = MemorySaver()

graph.add_node("chat_Node" , chat)

graph.add_edge(START , "chat_Node")
graph.add_edge("chat_Node" , END)

chatbot_workflows = graph.compile(checkpointer= checkpointer)