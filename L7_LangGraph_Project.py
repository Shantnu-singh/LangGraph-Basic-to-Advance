import streamlit as st
from L7_LangGraph_Project_backend import chatbot_workflows , HumanMessage , AIMessage , get_all_threads
import uuid

# Utility fucntions
def generate_thread_id():
    return uuid.uuid4()

def start_new_chat():
    new_thread_id = generate_thread_id()
    
    st.session_state['thread_id'] = new_thread_id
    add_thread_id(st.session_state['thread_id'])    

    st.session_state['msg_hist'] = []
    
def add_thread_id(thread_id):
    if thread_id not in st.session_state['thread_ids']:
        st.session_state['thread_ids'].append(thread_id)

def load_thread_id_chat(thread_id):
    config = {"configurable" : {"thread_id" : thread_id}}
    
    print(chatbot_workflows.get_state(config= config).values)
    if "msg" in chatbot_workflows.get_state(config= config).values:
        chat_hist = chatbot_workflows.get_state(config= config).values['msg']
    
        temp_msg = []
        
        for msg in chat_hist:
            if isinstance(msg , HumanMessage):
                role = "user"
            else:
                role = "assistant"
            temp_msg.append({"role" : role , "content" : msg.content})
            
        st.session_state['msg_hist'] = temp_msg
    else:
        st.session_state['msg_hist'] = []

    
    

# Streamlit session state is a Dict, after you press enter it stay that way
if "msg_hist" not in st.session_state:
    st.session_state['msg_hist'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()
    
if 'thread_ids' not in st.session_state:
    st.session_state['thread_ids'] = get_all_threads()

add_thread_id(st.session_state['thread_id'])

    
# Streamlit UI
st.title("Simple Chabot")

with st.sidebar:
    st.header("LangGraph Chatbot")
    if st.button("New Chat" , type= "primary"):
        start_new_chat()
    st.header("My Conversations")
    
    for thread_id in st.session_state['thread_ids'][::-1]:
        if st.button(str(thread_id)):
            st.session_state['thread_id'] = thread_id
            load_thread_id_chat(thread_id)


# Hist of all the msg
for msg in st.session_state['msg_hist']:
    with st.chat_message(msg['role']):
        st.text(msg['content'])
        


user_msg = st.chat_input("Type here....")

if user_msg:
    
    # Add msg to hist
    st.session_state['msg_hist'].append({'role' : "user", "content" : user_msg})
    with st.chat_message("user"):
        st.write(user_msg)
    
    
    # Reply from LLM
    config = {"configurable" : {"thread_id" : st.session_state['thread_id']}}

    # Instead of invoke use "stream" for streaming
    stream_reponce = chatbot_workflows.stream({"msg" : HumanMessage(content = user_msg)} , config = config , stream_mode="messages")
    
    with st.chat_message("assistant"):
        ai_msg = st.write_stream(msg_chunk.content for msg_chunk, _ in stream_reponce)
    
    st.session_state['msg_hist'].append({'role' : "assistant", "content" : AIMessage(content=ai_msg)})

