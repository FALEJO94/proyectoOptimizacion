import streamlit as st
import methods.differentiationIntegration as di

st.markdown("<h1 style='text-align: center'>Programación Lineal</h1>", unsafe_allow_html=True)
st.markdown("<h2>Parámetros</h2>", unsafe_allow_html=True)

st.sidebar.markdown('<h1>Métodos</h1>', unsafe_allow_html=True)

button__lineal = st.sidebar.button('Metodo Gráfico Prog. Lineal')
button__simplex = st.sidebar.button('Método Gráfico Simplex')