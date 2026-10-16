import streamlit as st
import requests

st.title("☁️ Previsão do Tempo")


chave_api = "chave_aqui" 

cidade = st.text_input("Digite o nome da cidade (Ex: São Paulo, Paris, Tokyo):")

if st.button("Buscar Clima"):

    if cidade.strip() != "":
        
        
        url_da_api = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"
        

        resposta = requests.get(url_da_api)

        if resposta.status_code == 200:
            

            dados_clima = resposta.json()
            
  
            temperatura = dados_clima["main"]["temp"]
            descricao = dados_clima["weather"][0]["description"]
            umidade = dados_clima["main"]["humidity"]
            sensacao = dados_clima["main"]["feels_like"]

            st.success(f"Clima atual em {cidade.title()}: {descricao.capitalize()}")
            st.write(f"Temperatura: {temperatura}°C")
            st.write(f"Umidade: {umidade}%")
            st.divider()
            st.subheader(f"Clima atual em {cidade.title()}: {descricao.capitalize()}")
            col1,col2,col3 = st.columns(3)
            with col1:
                st.metric(label='🌡️ Temperatura', value=f"{temperatura} °C")
            with col2:
                st.metric(label='🤔 Sensação termica', value=f"{sensacao} °C")
            with col3:
                st.metric(label='💧 Umidade', value=f"{umidade}%")

            if "chuva" in descricao:
                icone_gigante = "🌧️"
            elif "nuvem" in descricao or "nublado" in descricao:
                icone_gigante = "☁️"
            elif "limpo" in descricao or "sol" in descricao:
                icone_gigante = "☀️"
            elif "neve" in descricao:
                icone_gigante = "❄️"
            else:
                icone_gigante = "🌍"


            st.markdown(f"<h1 style='text-align: center; font-size: 100px;'>{icone_gigante}</h1>", unsafe_allow_html=True)            
                        
            
        else:

            st.error("Cidade não encontrada! Verifique o nome e tente novamente.")
            
    else:
        st.warning("Por favor, digite o nome de uma cidade.")

    sensao = dados_clima['main']['feels_like']
    