import streamlit as st
import methods.curvesInterpolation as cI

st.markdown("<h1 style='text-align: center'>Ajuste de Curvas e Interpolación 🖍️</h1>", unsafe_allow_html=True)
st.divider()
data_file = st.sidebar.file_uploader("Cargar archivo CSV", type=['csv'])

st.sidebar.markdown('<hr style="margin: 5px 0px 0px 0px;"><h1>Métodos</h1>', unsafe_allow_html=True)
button_square = st.sidebar.button('Mínimos Cuadrados')
button_lagrange = st.sidebar.button('Interpolación Lagrange')
button_splines = st.sidebar.button('Splines Cúbicos')
button_polynomial = st.sidebar.button('Regresión Polinomial')

if button_square:
    st.markdown("<h2>Mínimos Cuadrados</h2>", unsafe_allow_html=True)
    with st.spinner('Espera mientras que la magia hace lo suyo... 💫'):
        st.write(cI.smallSquares(data_file))

if button_lagrange:
    st.markdown("<h2>Interpolación Lagrange</h2>", unsafe_allow_html=True)
    with st.spinner('Espera mientras que la magia hace lo suyo... 💫'):
        st.write(cI.lagrange(data_file))

if button_splines:
    st.markdown("<h2>Splines Cúbicos</h2>", unsafe_allow_html=True)
    with st.spinner('Espera mientras que la magia hace lo suyo... 💫'):
        st.write(cI.splinesCubics(data_file))

if button_polynomial:
    st.markdown("<h2>Regresión Polinomial</h2>", unsafe_allow_html=True)
    with st.spinner('Espera mientras que la magia hace lo suyo... 💫'):
        st.write(cI.polynomialRegression(data_file))