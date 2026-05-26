import streamlit as st

st.title("🧠 Quiz Interativo de Conhecimentos Gerais")
st.write("Teste seus conhecimentos em diferentes áreas!")

# Lista de perguntas
perguntas = [
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["Londres", "Berlim", "Paris", "Roma"],
        "resposta": "Paris"
    },
    {
        "pergunta": "Quem escreveu 'Hamlet'?",
        "opcoes": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Leo Tolstoy"],
        "resposta": "William Shakespeare"
    },
    {
        "pergunta": "Qual é o elemento químico representado pelo símbolo 'O'?",
        "opcoes": ["Ouro", "Oxigênio", "Prata", "Ferro"],
        "resposta": "Oxigênio"
    },
    # Adicione mais perguntas conforme desejar
]

if 'respostas' not in st.session_state:
    st.session_state.respostas = {}

# Exibe as perguntas
for idx, item in enumerate(perguntas):
    with st.expander(f"Pergunta {idx + 1}"):
        st.write(item["pergunta"])
        resposta_usuario = st.radio(
            "Escolha uma opção:",
            item["opcoes"],
            key=f"pergunta_{idx}"
        )
        st.session_state.respostas[f"pergunta_{idx}"] = resposta_usuario

st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        height: 3em;
        width: 100%;
        border-radius:10px;
        border:2px solid #4CAF50;
        font-size:17px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Ver Resultado"):
    acertos = 0
    for idx, item in enumerate(perguntas):
        resposta_correta = item["resposta"]
        resposta_usuario = st.session_state.respostas.get(f"pergunta_{idx}")

        if resposta_usuario == resposta_correta:
            acertos += 1
            st.success(f"✅ Pergunta {idx + 1}: Correto!")
        else:
            st.error(f"❌ Pergunta {idx + 1}: Incorreto! A resposta correta é '{resposta_correta}'.")

    st.write(f"**Você acertou {acertos} de {len(perguntas)} perguntas.**")
    if acertos == len(perguntas):
        st.balloons()
