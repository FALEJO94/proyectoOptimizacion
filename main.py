import streamlit as st
import os

# st.set_page_config(layout="wide")
ruta_absoluta = 'https://drive.google.com/file/d/1PspWCEqPO-0NdbRz3zpnkQdMrgmt9UHg/view?usp=drive_link'
# ruta_absoluta = os.path.abspath('./src/files/manual_usuario_pt.pdf')

st.markdown("<h1 style='text-align: center;'>Métodos Numéricos y Optimización 🤘💥</h1>", unsafe_allow_html=True)
st.markdown("<h3>Vamos allá!! 🤪</h3><hr style='margin: 5px 0px;'>", unsafe_allow_html=True)
st.markdown("<h5 style='margin-top: 30px; line-height: 35px'>- Bienvenidos a nuestra web. Los métodos numéricos y la optimización son pilares fundamentales en la resolución de problemas complejos en diversas áreas. Su importancia radica en la capacidad de proporcionar herramientas eficientes para aproximarse a soluciones precisas en situaciones donde el análisis exacto resulta impracticable. Estas disciplinas no solo facilitan la toma de decisiones informadas en campos como la ingeniería, la ciencia y la economía, sino que también posibilitan la modelización de sistemas complejos y el desarrollo de tecnologías avanzadas -</h5><h5 style='margin-top: 30px; line-height: 35px'>A continuación encontraremos algunos métodos numéricos y de optimización los cuales son interactivos. Al final de de la web, encontraremos un manual de usuario</h5><hr style='margin: 5px 0px;'>", unsafe_allow_html=True)
st.markdown("<h3>Creado por 🤓</h3>", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image('./src/img/1.jpg', caption='Esteban Zuluaga (Estudiante UAM)', width=300)
    with col2:
        st.image('./src/img/2.jpg', caption='Fredy Alejandro (Estudiante UAM)', width=340)

st.markdown("<h3>Inspirada por 😎</h3>", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image('./src/img/3.png', caption='Reinel Tabares (Profesor UAM)', width=300)
    with col2:
        st.image('./src/img/4.png', caption='Johan Sebastian (Desarrollador AI)', width=300)

st.markdown("<hr style='margin: 5px 0px;'><h3>Pagina Oficial 💻</h3>", unsafe_allow_html=True)
st.write("[Métodos Numéricos y Optimización](https://bioaiteamlearning.github.io/Metodos_2023_03_UAM/intro.html)")

st.markdown("<hr style='margin: 5px 0px;'><h3>Manual de usuario 👀</h3>", unsafe_allow_html=True)
st.markdown(f"<a href='{ruta_absoluta}' target='_blank'>Métodos Numéricos y Optimización 🤘💥</a>", unsafe_allow_html=True)