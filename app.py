import streamlit as st
import openai

# Configuração da chave da API
openai.api_key = "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"

# Estilo para esconder o cabeçalho e rodapé
st.markdown("""
    <style>
        #MainMenu, header, footer {visibility: hidden;}
        .block-container {padding-top: 2rem;}
    </style>
""", unsafe_allow_html=True)

# Inicializa o histórico na sessão
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Barra lateral com histórico
with st.sidebar:
    st.markdown("## Histórico")
    for i, item in enumerate(st.session_state.chat_history):
        st.markdown(f"**{i+1}.** {item['user']}")
    st.markdown("## Idioma")
    st.selectbox("Escolha o idioma", ["Português", "English", "Español"], index=0)

# Título
st.title("Chat com IA")

# Entrada do usuário
user_input = st.text_input("Digite sua pergunta aqui e pressione Enter:", key="input", label_visibility="collapsed")

# Quando o usuário envia uma pergunta
if user_input:
    try:
        # Envia a pergunta para o modelo GPT-3.5
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        answer = response["choices"][0]["message"]["content"]

        # Armazena no histórico
        st.session_state.chat_history.append({"user": user_input, "ai": answer})

        # Limpa a pergunta e mostra só a resposta
        st.experimental_rerun()
    except Exception as e:
        st.error(f"Erro ao chamar API: {e}")

# Mostra apenas a última resposta
if st.session_state.chat_history:
    st.write(f"**IA:** {st.session_state.chat_history[-1]['ai']}")
