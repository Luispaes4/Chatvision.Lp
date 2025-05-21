import streamlit as st
import openai
from openai import OpenAI

client = OpenAI(api_key="sk-...")  # Substitua pela sua chave

st.set_page_config(page_title="ChatVision", layout="wide")

st.markdown("""
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding-top: 1rem;}
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("Histórico")
    if "history" not in st.session_state:
        st.session_state.history = []
    for msg in st.session_state.history[::-1]:
        st.markdown(f"- {msg[:40]}...")

    lang = st.selectbox("Idioma", ["Português", "English"])
    st.session_state.lang = lang

prompt = st.chat_input("Digite sua pergunta")

if prompt:
    st.session_state.history.append(prompt)
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente útil."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.markdown(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Erro: {e}")
