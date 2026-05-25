import streamlit as st

st.title('Hello, FIAP!')
st.write('Let`s Rock the Future!')

# Barra de Progresso
import time

progresso = st.progress(0)
for i in range(100):
    time.sleep(0.02)
    progresso.progress(i + 1)
st.write("Progresso completo!")

# Indicador de Carregamento
with st.spinner("Carregando..."):
    time.sleep(2)
st.success("Carregamento concluído!")

# Mensagens de feedback visual ao usuário
st.success("Operação realizada com sucesso!")
st.error("Ocorreu um erro!")
st.warning("Atenção! Verifique os dados.")
st.info("Para mais informações, consulte a documentação.")

# Animação de Balões
if st.button("Mostrar balões"):
    st.balloons()
