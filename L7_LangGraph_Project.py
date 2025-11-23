import streamlit as st
from L7_LangGraph_Project_backend import chatbot_workflows , HumanMessage 
st.title("Simple Chabot")

# Utility Fucntion

# Streamlit session state is a Dict, after you press enter it stay that way
if "msg_hist" not in st.session_state:
    st.session_state['msg_hist'] = []



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
    config = {"configurable" : {"thread_id" : "1"}}

    # Instead of invoke use "stream" for streaming
    stream_reponce = chatbot_workflows.stream({"msg" : HumanMessage(content = user_msg)} , config = config , stream_mode="messages")
    
    with st.chat_message("assistant"):
        ai_msg = st.write_stream(msg_chunk.content for msg_chunk, _ in stream_reponce)
    
    st.session_state['msg_hist'].append({'role' : "assistant", "content" : ai_msg})

