import streamlit as st
import openai
import requests

# Chave da API OpenAI
openai.api_key = "sk-..."  # Substitua pela sua chave GPT-3.5

# ALTCHA
ALTCHA_PUBLIC_KEY = "ckey_016c237681e746bad673fe063dce"

st.set_page_config(page_title="ChatVision", layout="wide")

st.markdown("""
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding-top: 1rem;}
    </style>
""", unsafe_allow_html=True)

# Sidebar - Histórico + Idioma
with st.sidebar:
    st.title("Histórico")
    if "history" not in st.session_state:
        st.session_state.history = []
    for msg in st.session_state.history[::-1]:
        st.markdown(f"- {msg[:40]}...")

    lang = st.selectbox("Idioma", ["Português", "English"])
    st.session_state.lang = lang

# Campo de texto
prompt = st.chat_input("Digite sua pergunta")

# Função para verificação ALTCHA
def verify_altcha():
    # Aqui você pode adicionar verificação real se quiser
    return True

# Resposta da IA
if prompt:
    if verify_altcha():
        st.session_state.history.append(prompt)
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Você é um assistente útil."},
                        {"role": "user", "content": prompt}
                    ]
                )
                answer = response.choices[0].message.content
                st.markdown(answer)
            except Exception as e:
                st.error(f"Erro: {e}")
    else:
        st.error("Falha na verificação ALTCHA.")
  
