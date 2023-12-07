import streamlit as st
import methods.ordinaryDifferential as od

st.markdown("<h2 style='text-align: center'>Ecuaciones Diferenciales Ordinarias 🥵</h2>", unsafe_allow_html=True)
st.markdown("<h3>Parámetros</h3>", unsafe_allow_html=True)

st.sidebar.markdown('<h1>Métodos</h1>', unsafe_allow_html=True)

button__runge_3 = st.sidebar.button('Runge Kutta Orden 3')
button__runge_4 = st.sidebar.button('Runge Kutta Orden 4')
button__predator = st.sidebar.button('Depredador Presa')

with st.expander("Runge Kutta"):
    col1, col2, col3 = st.columns(3)

    with col1:
        init_i = st.number_input("Valor Corriente", 0.0, 20.0, 0.1, 0.1)
        r = st.number_input("Resistencia", 0.0, 20.0, 1.0, 0.1)
        c = st.number_input("Capacitor", 0.0, 20.0, 1.0, 0.1)

    with col2:
        init_v = st.number_input("Valor Voltaje", 0.0, 20.0, 0.1, 0.1)
        i = st.number_input("Inductancia", 0.0, 20.0, 0.5, 0.1)

    with col3:
        t_range = st.number_input("Rango Tiempo", 0.0, 20.0, 10.0, 0.1)
        v = st.number_input("Voltaje Fuente", 0.0, 20.0, 1.0, 0.1)


with st.expander("Depredador - Presa"):
    colD1, colD2, colD3, colD4 = st.columns(4)

    with colD1:
        alpha = st.number_input("Tasa Crecimiento Presas", 0.0, 10.0, 1.1, 0.1)
        x0 = st.number_input("Cantidad Presas", 0, 100, 10, 1)
        h = st.number_input("Paso del Tiempo", 0.0, 10.0, 0.01, 0.1)
    with colD2:
        beta = st.number_input("Tasa Mortalidad Presas", 0.0, 10.0, 0.4, 0.1)
        y0 = st.number_input("Cantidad Depredadores", 0, 100, 10, 1)
    with colD3:
        gamma = st.number_input("Tasa Creci. Depredador", 0.0, 10.0, 0.4, 0.1)
        t0 = st.number_input("Tiempo Inicial", 0, 100, 0, 1)
    with colD4:
        delta = st.number_input("Tasa Creci. Depre. X Presa", 0.0, 10.0, 0.1, 0.1)
        t_max = st.number_input("Tiempo Máximo", 0, 100, 50, 1)

if button__runge_3:
    st.markdown("<h2>Runge Kutta Orden 3</h2>", unsafe_allow_html=True)
    with st.spinner('Espera mientras que la magia hace lo suyo... 💫'):
        st.write(od.rungeKutta3(init_i, init_v, t_range))

if button__runge_4:
    st.markdown("<h2>Runge Kutta Orden 4</h2>", unsafe_allow_html=True)
    with st.spinner('Espera mientras que la magia hace lo suyo... 💫'):
        st.write(od.rungeKutta4(init_i, init_v, t_range, r, c, i, v))

if button__predator:
    st.markdown("<h2>Depredador - Presa</h2>", unsafe_allow_html=True)
    with st.spinner('Espera mientras que la magia hace lo suyo... 💫'):
        st.write(od.predatorPrey(x0, y0, alpha, beta, gamma, delta, h, t0, t_max))