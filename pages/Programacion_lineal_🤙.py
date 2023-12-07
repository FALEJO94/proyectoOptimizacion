import streamlit as st
import methods.linearProgramming as lp

st.markdown("<h1 style='text-align: center'>Programación Lineal</h1>", unsafe_allow_html=True)
st.markdown("<h2>Parámetros</h2>", unsafe_allow_html=True)

st.sidebar.markdown('<h1>Métodos</h1>', unsafe_allow_html=True)

button__graphic = st.sidebar.button('Metodo Gráfico Prog. Lineal')
button__simplex = st.sidebar.button('Método Gráfico Simplex')

with st.expander("Metodo Gráfico Programación Lineal"):
    col1, col2, col3 = st.columns(3)

    with col1:
        f = st.text_input("Función", '3 * x + 4 * y')

    with col2:
        r = st.text_input("Restricciones", ['2 * x + y - 20', 'x + 2 * y - 16'])

    with col3:
        v = st.text_input("Variables", ['x', 'y'])

with st.expander("Método Gráfico Simplex"):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        vc = st.text_input("Vertices", '4 2, 8 1, 2 5')

    with col2:
        c = st.text_input("Coeficientes", '1 1, -2 1, 1 -2')

    with col3:
        ct = st.text_input("Constantes", '7 5 19')

    with col4:
        s = st.text_input("Sign", "<= >= <=")

if button__graphic:
    st.markdown("<h2>Metodo Gráfico Programación Lineal</h2>", unsafe_allow_html=True)
    with st.spinner('Ejecutando...'):
        st.write(lp.graphicalMethod(f, r, v))

if button__simplex:
    st.markdown("<h2>Método Gráfico Simplex</h2>", unsafe_allow_html=True)
    st.write(lp.simplexMethod(vc, c, ct, s))