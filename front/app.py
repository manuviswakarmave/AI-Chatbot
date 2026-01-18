import streamlit as st
import requests

st.set_page_config(page_title="AI Chatbot", page_icon="<UNK>", layout="centered")
st.title("AI Chatbot")
st.markdown("Chat with AI")

with st.sidebar:
    st.header("AI Chatbot Configuration")
    model_provider = st.selectbox("model provider", ["Groq"])
    model_name = st.selectbox("model name", ["llama-3.3-70b-versatile"])
    system_prompt = st.text_area("System Prompt", value = "Act as a personal smart AI assistant", height =100)
    allow_search =st.checkbox("Allow web search", value = True)

#session state for chat History

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#display chat

for role, msg in st.session_state.chat_history:
    if role== "User":
        with st.chat_message("User"):
            st.markdown(msg)

    else:
        with st.chat_message("ai"):
            st.markdown(msg)

#handle user input

user_query= st.chat_input("Enter youy Query")
if user_query:
    with st.chat_message("User"):
        st.markdown(user_query)
    st.session_state.chat_history.append(("User",user_query))

    #send backend request

    with st.chat_message("ai"):
        with st.spinner("Thinking...."):
            try:
                payload = {
                    "model_name" : model_name,
                    "model_provider" : model_provider,
                    "system_prompt" : system_prompt,
                    "messages": [user_query],
                    "allow_search" : allow_search

                }
                print("reached here")
                res = requests.post("http://127.0.0.1:8000/chat", json=payload)
                print(res)
                response = res.json()
                st.markdown(response)
                st.session_state.chat_history.append(("ai",response))
            except Exception as e:
                st.error(f"Error: {e}")




