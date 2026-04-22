import streamlit as st
from utils import call_llama


st.title(":speech_balloon: Llama Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Llama :llama:")
    
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
    
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    prompt += """\n\nMake the response as short as possible."""
    with st.spinner("Generating response..."):
        msg = call_llama("qwen2.5:3b-instruct", prompt)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    
if __name__ == "__main__":
    call_llama("qwen2.5:3b-instruct", "Hi", stream=True)