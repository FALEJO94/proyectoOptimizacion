import streamlit as st
import methods.rootCalculation as rC

# st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center'>Calculo de raices</h1>", unsafe_allow_html=True)
st.markdown("<h2>Parámetros</h2>", unsafe_allow_html=True)

# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.1)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 2.0)
st.sidebar.markdown('<hr style="margin: 5px 0px 0px 0px;"><h1>Métodos</h1>', unsafe_allow_html=True)
button_biseccion = st.sidebar.button('Método de la Bisección')
button_false_pos = st.sidebar.button('Método de la Falsa Posición')
button_newton = st.sidebar.button('Método de Newton-raphson')
button_secante = st.sidebar.button('Método de Secante')
button_variante = st.sidebar.button('Método Variante Secante')
button_punto_fijo = st.sidebar.button('Método Punto Fijo')

col1, col2, col3, col4, col5 = st.columns(5)

# Ingresar los límites
with col1:
    xl = st.number_input("Límite Inferior", -10.0, 20.0, 0.2, 0.1)
    xi = st.number_input("Punto Inicial", -10.0, 20.0, 0.75, 0.1)

with col2:
    xu = st.number_input("Límite Superior", -10.0, 20.0, 1.7, 0.1)
    max_iteration = st.number_input("Interacciones Máximas", 0.0, 5000.0, 1000.0, 0.1)

with col3:
    var = st.text_input("Variable", "x")
    init_val = st.number_input("Valor Incial", 0.0, 3.0, 0.5, 0.1)

with col4:
    tol = st.number_input("Tolerancia", 0.0, 2.0, 0.5, 0.00)

# Ingresar la función
with col5:
    func = st.text_input("Función", "x**3 - x")

st.divider()

if button_biseccion:
    st.markdown("<h2>Método de la Bisección</h2>", unsafe_allow_html=True)
    st.write(rC.bisectionMethod(func, xl, xu, tol,start_range,end_range, var))

if button_false_pos:
    st.markdown("<h2>Método de la Falsa Posición</h2>", unsafe_allow_html=True)
    st.write(rC.falsePositioning(func, xl, xu, tol,start_range,end_range, var))

if button_newton:
    st.markdown("<h2>Método de Newton-raphson</h2>", unsafe_allow_html=True)
    st.write(rC.newtonRaphsonMethod(func, xi, tol,start_range,end_range, var))

if button_secante:
    st.markdown("<h2>Método de la Secante</h2>", unsafe_allow_html=True)
    st.write(rC.secantMethod(func, xl, xu, tol,start_range,end_range, var))

if button_variante:
    st.markdown("<h2>Método Variante de la Secante</h2>", unsafe_allow_html=True)
    st.write(rC.variantSecantMethod(func, xl, xu, tol,start_range,end_range, var, max_iteration))

if button_punto_fijo:
    st.markdown("<h2>Método Punto Fijo</h2>", unsafe_allow_html=True)
    st.write(rC.fixedPoint(func, xl, xu, tol,start_range,end_range, var, max_iteration, init_val))

