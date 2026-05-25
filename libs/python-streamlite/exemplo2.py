import streamlit as st

st.title('Hello, FIAP!')
st.write('Let`s Rock the Future!')

# widgets de entrada

# Entrada de Texto
nome = st.text_input("Digite seu nome:")
if nome:
    st.write(f"Olá, {nome}!")

# Área de Texto
comentario = st.text_area("Deixe seu comentário:")
if comentario:
    st.write(f"Comentário enviado: {comentario}")

# Entrada Numérica
idade = st.number_input("Informe sua idade:", min_value=0, max_value=120, value=25)
st.write(f"Idade informada: {idade}")

# Carregamento de Arquivos
arquivo = st.file_uploader("Envie um arquivo de texto:", type=["txt"])
if arquivo is not None:
    conteudo = arquivo.read().decode("utf-8")
    st.write(conteudo)
