from dotenv import load_dotenv 
from langchain_google_genai import ChatGoogleGenerativeAI 
import streamlit as st

load_dotenv() 

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=0.2, max_output_tokens=1024) 
st.title("QnA Bot")
st.subheader("Ask me anything about the topic you want to know!")

if "messages" not in st.session_state:
    st.session_state.messages =[]

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask anything")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").write(query)
    response=llm.invoke(query)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    st.chat_message("assistant").markdown(response.text)
