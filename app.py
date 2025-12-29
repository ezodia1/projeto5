import streamlit as st
import pandas as pd
import plotly_express as px

# carregar os dados
car_data = pd.read_csv('notebooks/vehicles.csv')

st.title('Análise de anúncios de veículos')

# botão 1 — histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma da quilometragem dos veículos')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# botão 2 — gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão entre preço e quilometragem')
    fig_scatter = px.scatter(
        car_data,
        x='odometer',
        y='price'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
