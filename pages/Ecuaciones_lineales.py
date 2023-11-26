import streamlit as st
import methods.linearEquations as lE

st.markdown("<h1 style='text-align: center'>Ecuaciones Lineales</h1>", unsafe_allow_html=True)
st.markdown("<h2>Parámetros</h2>", unsafe_allow_html=True)

button_gaussiana = st.sidebar.button('Eliminación Gaussiana')
button_triangular = st.sidebar.button('Sistema Lineal Triangular Superior')
button_pivot = st.sidebar.button('Pivoteo')

col1, col2, col3 = st.columns(3)

with col1:
    matriz = st.text_input("Matriz", [[2.0, 3.0, -1.0],[4.0, 4.0, -3.0], [4.0, 3.0, -2.0]])

with col2:
    vector = st.text_input("Vector", [6.0, 3.0, 5.0]) 

with col3:
    solution = st.text_input("Solución conocida", [1.0, 2.0, 3.0]) 

if button_gaussiana:
    st.markdown("<h2>Eliminación Gaussiana</h2>", unsafe_allow_html=True)
    st.write(lE.gaussiana(matriz, vector, solution))

if button_triangular:
    st.markdown("<h2>Sistema Lineal Triangular Superior</h2>", unsafe_allow_html=True)
    st.write(lE.linealTriangular(matriz, vector, solution))

if button_pivot:
    st.markdown("<h2>Pivoteo</h2>", unsafe_allow_html=True)
    st.write(lE.pivot(matriz, vector, solution))