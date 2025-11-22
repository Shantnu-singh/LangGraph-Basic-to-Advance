import streamlit as st
st.title("Simple Chabot")

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
    
    st.session_state['msg_hist'].append({'role' : "assistant", "content" : user_msg})
    with st.chat_message("assistant"):
        st.write(user_msg)