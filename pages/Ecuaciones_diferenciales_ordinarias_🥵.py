import streamlit as st
import methods.differentiationIntegration as di

st.markdown("<h1 style='text-align: center'>Ecuaciones Diferenciales Ordinarias</h1>", unsafe_allow_html=True)
st.markdown("<h2>Parámetros</h2>", unsafe_allow_html=True)

st.sidebar.markdown('<h1>Métodos</h1>', unsafe_allow_html=True)

button__runge_3 = st.sidebar.button('Runge Kutta Orden 3')
button__runge_4 = st.sidebar.button('Runge Kutta Orden 4')
button__predator = st.sidebar.button('Depredador Presa')