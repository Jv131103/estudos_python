import streamlit as st

st.title('Hello, FIAP!')
st.write('Let`s Rock the Future!')

# widgets de iteração

# Botão de Ação
if st.button("Clique aqui"):
    st.write("Você clicou no botão!")

# Caixa de Seleção (checkbox)
aceitar = st.checkbox("Eu aceito os termos e condições.")
if aceitar:
    st.write("Obrigado por aceitar os termos!")

# Botões de Rádio
cor = st.radio("Escolha sua cor favorita:", ["Azul", "Verde", "Vermelho"])
st.write(f"Você escolheu: {cor}")

# Caixa de Seleção (selectbox)
fruta = st.selectbox("Escolha uma fruta:", ["Maçã", "Banana", "Laranja"])
st.write(f"Você escolheu: {fruta}")

# Controle Deslizante
altura = st.slider("Escolha sua altura:", min_value=1.0, max_value=2.5, value=1.75)
st.write(f"Sua altura: {altura} metros")

# Seleção Múltipla
hobbies = st.multiselect("Escolha seus hobbies favoritos:", ["Ler", "Esportes", "Música", "Viagens"])
st.write(f"Você escolheu: {', '.join(hobbies)}")
