import streamlit as st
import methods.differentiationIntegration as di

st.markdown("<h1 style='text-align: center'>Diferenciación e Integración 👊</h1>", unsafe_allow_html=True)
st.markdown("<h2>Parámetros</h2>", unsafe_allow_html=True)

start_range = st.sidebar.slider("Inicio del rango", -10.0, 10.0, 0.1)
end_range = st.sidebar.slider("Fin del rango", -10.0, 10.0, 2.0)

st.sidebar.markdown('<hr style="margin: 5px 0px 0px 0px;"><h1>Métodos</h1>', unsafe_allow_html=True)
button_euler = st.sidebar.button('Euler para Integración Númerica')
button_trapezoid = st.sidebar.button('Regla Trapezoidal')
button_mul_trapezoid = st.sidebar.button('Regla Trapezoidal Múltiple')
button_simpson1 = st.sidebar.button(f'Regla Simpson 1/3')
button_simpson3 = st.sidebar.button(f'Regla Simpson 3/8')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    var = st.text_input("Variable", "t")
    func = st.text_input("Función", "3*t**2")

with col2:
    ti = st.number_input("Tiempo Inicial", -10.0, 20.0, -2.0, 0.1)
    a = st.number_input("Limite a", -10.0, 20.0, 1.0, 0.1)

with col3:
    tf = st.number_input("Tiempo Final", -10.0, 20.0, 2.0, 0.1)
    b = st.number_input("Limite b", -10.0, 20.0, 2.0, 0.1)

with col4:
    h = st.number_input("Paso Integración", -10.0, 20.0, 0.2, 0.1)
    n = st.number_input("Total de trapecios", 1, 20, 2, 1)

with col5:
    y0 = st.number_input("Condición Inicial", -10.0, 20.0, 0.00, 0.1)

st.divider()

if button_euler:
    st.markdown("<h2>Euler para Integración Númerica</h2>", unsafe_allow_html=True)
    st.write(di.eulerMethod(var, func, ti, tf, h, y0))

if button_trapezoid:
    st.markdown("<h2>Regla Trapezoidal</h2>", unsafe_allow_html=True)
    st.write(di.trapezoid(var, func, a, b, start_range, end_range))

if button_mul_trapezoid:
    st.markdown("<h2>Regla Trapezoidal Múltiple</h2>", unsafe_allow_html=True)
    st.write(di.multipleTrapezoid(var, func, a, b, start_range, end_range, n))

if button_simpson1:
    st.markdown("<h2>Regla Simpson 1/3</h2>", unsafe_allow_html=True)
    st.write(di.simpson1_3(var, func, a, b, start_range, end_range))

if button_simpson3:
    st.markdown("<h2>Regla Simpson 3/8</h2>", unsafe_allow_html=True)
    st.write(di.simpson1_3(var, func, a, b, start_range, end_range))