import streamlit as st
import openai

# Chave da API
openai.api_key = "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"

# Estilo para esconder menus
st.markdown("""
    <style>
        #MainMenu, header, footer {visibility: hidden;}
        .block-container {padding-top: 2rem;}
    </style>
""", unsafe_allow_html=True)

# Inicializa histórico
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Barra lateral com histórico e idiomas
with st.sidebar:
    st.markdown("## Histórico")
    for i, item in enumerate(st.session_state.chat_history):
        st.markdown(f"**{i+1}.** {item['user']}")
    st.markdown("## Idioma")
    st.selectbox("Escolha o idioma", ["Português", "English", "Español"], index=0)

# Título
st.title("Chat com GPT-3.5")

# Entrada
user_input = st.text_input("Digite sua pergunta e pressione Enter:", key="input", label_visibility="collapsed")

# Envia para a IA
if user_input:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é uma IA útil que responde em português."},
                {"role": "user", "content": user_input}
            ]
        )
        resposta = response.choices[0].message["content"]
        st.session_state.chat_history.append({"user": user_input, "ai": resposta})
        st.experimental_rerun()

    except Exception as e:
        st.error(f"Erro: {e}")

# Mostra última resposta
if st.session_state.chat_history:
    st.write(f"**IA:** {st.session_state.chat_history[-1]['ai']}")
