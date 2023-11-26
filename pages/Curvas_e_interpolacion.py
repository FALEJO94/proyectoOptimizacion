import streamlit as st
import methods.curvesInterpolation as cI

st.markdown("<h1 style='text-align: center'>Ajuste de Curvas e Interpolación</h1>", unsafe_allow_html=True)
# st.markdown("<h2>Parámetros</h2>", unsafe_allow_html=True)
st.divider()
data_file = st.sidebar.file_uploader("Cargar archivo CSV", type=['csv'])
st.sidebar.divider()

button_square = st.sidebar.button('Mínimos Cuadrados')
button_lagrange = st.sidebar.button('Interpolación Lagrange')
button_splines = st.sidebar.button('Splines Cúbicos')
button_polynomial = st.sidebar.button('Regresión Polinomial')

if button_square:
    st.markdown("<h2>Mínimos Cuadrados</h2>", unsafe_allow_html=True)
    st.write(cI.smallSquares(data_file))

if button_lagrange:
    st.markdown("<h2>Interpolación Lagrange</h2>", unsafe_allow_html=True)
    st.write(cI.lagrange(data_file))

if button_splines:
    st.markdown("<h2>Splines Cúbicos</h2>", unsafe_allow_html=True)
    st.write(cI.splinesCubics(data_file))

if button_polynomial:
    st.markdown("<h2>Regresión Polinomial</h2>", unsafe_allow_html=True)
    st.write(cI.polynomialRegression(data_file))