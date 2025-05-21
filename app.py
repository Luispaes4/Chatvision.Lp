import openai
import streamlit as st
import os
from dotenv import load_dotenv

# Carrega a chave da API do arquivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configuração da página
st.set_page_config(layout="wide", page_title="ChatVision GPT-3.5")

# Oculta o topo e aplica tema escuro com CSS
st.markdown("""
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding-top: 2rem;}
    </style>
""", unsafe_allow_html=True)

# Sidebar com histórico e seleção de idioma
with st.sidebar:
    st.title("ChatVision")
    st.markdown("**Histórico:**")
    if "history" not in st.session_state:
        st.session_state.history = []
    for i, h in enumerate(reversed(st.session_state.history[-10:])):
        st.markdown(f"{i+1}. {h[:40]}...")

    lang = st.selectbox("Idioma da resposta:", ["pt", "en", "es"], index=0)

st.title("ChatGPT 3.5")

# Caixa de entrada
prompt = st.text_input("Digite sua pergunta:", key="user_input")

if prompt:
    try:
        # Remove prompt após envio
        st.session_state.history.append(prompt)
        st.session_state.user_input = ""

        with st.spinner("Pensando..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"Responda no idioma '{lang}'."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response.choices[0].message.content
            st.markdown(f"**Resposta:**\n{reply}")

    except Exception as e:
        st.error(f"Erro: {e}")
        
