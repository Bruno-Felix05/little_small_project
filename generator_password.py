import streamlit as st
import random
import string

st.title("🔐 Gerador de Senhas Seguras")


# slider para o tamanho da senha
tamanho = st.slider('Slider', min_value=6, max_value=32, value=12)
# checkbox para as opções (Maiúsculas, Números, Símbolos)
usar_numeros = st.checkbox('Incluir Numeros')
usar_maiusculo = st.checkbox('Incluir letras maiusculas')
usar_simbolos = st.checkbox('Incluir simbolos')


if st.button("Gerar Senha"):
    
    # sorteio começa apenas com letras minúsculas
    caracteres_disponiveis = string.ascii_lowercase 
    
    # marcou a caixinha de números, adiciona os números 
    if usar_numeros:
        caracteres_disponiveis = caracteres_disponiveis + string.digits

    if usar_maiusculo:
        caracteres_disponiveis = caracteres_disponiveis + string.ascii_uppercase

    if usar_simbolos:
        caracteres_disponiveis = caracteres_disponiveis + string.punctuation

    

    lista_senha = random.choices(caracteres_disponiveis, k=tamanho)
    senha = ''.join(lista_senha)

    st.success("Senha gerada com sucesso!")
    st.code(senha)