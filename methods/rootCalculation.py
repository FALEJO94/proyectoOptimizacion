import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import pandas as pd
from math import e

def calculate_y(x_values, expression):
  return [expression.subs({x: xi}) for xi in x_values]

def bisectionMethod(func, xl, xu, tol, start_range, end_range, var):
  # Tolerancia y valores iniciales
  global x
  xr = None
  xr_ant = xu
  error = tol + 1
  it = 1
  x = sp.symbols(var)
  y = sp.sympify(func)

  # Dataframe para almacenar los resultados
  columnas = ['Xl', 'Xu', 'Xr', 'er(%)', 'f(Xl)', 'f(Xu)', 'f(Xr)']
  tabla = pd.DataFrame(columns=columnas)

  # Espacio reservado para la figura
  fig_placeholder = st.empty()
  tablita = st.empty()
  fig_placeholder.markdown(
    """
    <style>
    div[data-testid="stBlock"] {
        width: 200px;
    }
    </style>
    """, unsafe_allow_html=True)
  
  while error > tol:
    # Evaluamos la función en los puntos del intervalo
    fxl = y.subs({x: xl}).evalf()
    fxu = y.subs({x: xu}).evalf()

    # Crear la figura
    fig, ax = plt.subplots()
    r = np.linspace(start_range, end_range, 100)
    fx = calculate_y(r, y)

    ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
    ax.vlines(x=0, ymin=min(fx)-0.5, ymax=max(fx)+0.5, color='k')
    ax.hlines(y=0, xmin=min(r)-0.5, xmax=max(r)+0.5, color='k')
    ax.set_title(f"${sp.latex(y)}$")
    ax.grid()

    # Límites xl y xu
    ax.vlines(x=xl, ymin=0, ymax=fxl, color='k', linestyle='--', label=f'$x_l=${xl}')
    ax.vlines(x=xu, ymin=0, ymax=fxu, color='k', linestyle='--', label=f'$x_u=${xu}')

    # Calculamos la raíz
    xr = round((xl + xu) / 2, 4)
    fxr = y.subs({x: xr}).evalf()

    # Pintamos el punto intermedio
    ax.plot(xr, fxr, 'ro', label=f'Raíz={xr}')
    ax.legend()

    # Actualizamos el error y la tabla
    error = np.abs((xr - xr_ant) / xr) * 100 if xr != 0 else 0
    nueva_fila = {'Xl': xl, 'Xu': xu, 'Xr': xr, 'er(%)': error, 'f(Xl)': fxl, 'f(Xu)': fxu, 'f(Xr)': fxr}
    tabla = pd.concat([tabla, pd.DataFrame([nueva_fila])], ignore_index=True)
    # Actualizamos los límites
    if fxl * fxr < 0:
      xu = xr
    elif fxl * fxr > 0:
      xl = xr
    else:
      st.success(f"La raíz está en: ({round(xr,4)}, {round(fxr,4)})")
      break

    xr_ant = xr
    it += 1

    # Mostrar la figura en el espacio reservado
    fig_placeholder.pyplot(fig)
    tablita.dataframe(tabla)
    # Borra la figura para la siguiente iteración
    plt.close(fig)

def falsePositioning(func, xl, xu, tol, start_range, end_range, var):
  global x
  xr = None
  xr_ant = xu
  error = tol + 1
  it = 1
  x = sp.symbols(var)
  y = sp.sympify(func)

  # Dataframe para almacenar los resultados
  columnas = ['Xl', 'Xu', 'Xr', 'er(%)', 'f(Xl)', 'f(Xu)', 'f(Xr)']
  tabla = pd.DataFrame(columns=columnas)

  # Espacio reservado para la figura
  fig_placeholder = st.empty()
  tablita = st.empty()
  fig_placeholder.markdown(
    """
    <style>
    div[data-testid="stBlock"] {
        width: 200px;
    }
    </style>
    """,
    unsafe_allow_html=True)
  while error > tol:
    # Evaluamos la función en los puntos del intervalo
    fxl = y.subs({x: xl}).evalf()
    fxu = y.subs({x: xu}).evalf()

    # Crear la figura
    fig, ax = plt.subplots()
    r = np.linspace(start_range, end_range, 100)
    fx = calculate_y(r, y)

    ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
    ax.vlines(x=0, ymin=min(fx)-0.5, ymax=max(fx)+0.5, color='k')
    ax.hlines(y=0, xmin=min(r)-0.5, xmax=max(r)+0.5, color='k')
    ax.set_title(f"${sp.latex(y)}$")
    ax.grid()

    # Límites xl y xu
    ax.vlines(x=xl, ymin=0, ymax=fxl, color='k', linestyle='--', label=f'$x_l=${xl}')
    ax.vlines(x=xu, ymin=0, ymax=fxu, color='k', linestyle='--', label=f'$x_u=${xu}')

    # Calculamos la raíz
    xr = round(((fxl * xu) - (fxu * xl)) / (fxl - fxu), 4)
    fxr = y.subs({x: xr}).evalf()

    # Pintamos el punto intermedio
    ax.plot(xr, fxr, 'ro', label=f'Raíz={xr}')
    ax.legend()

    # Actualizamos el error y la tabla
    error = np.abs((xr - xr_ant) / xr) * 100 if xr != 0 else 0
    nueva_fila = {'Xl': xl, 'Xu': xu, 'Xr': xr, 'er(%)': error, 'f(Xl)': fxl, 'f(Xu)': fxu, 'f(Xr)': fxr}
    tabla = pd.concat([tabla, pd.DataFrame([nueva_fila])], ignore_index=True)
    # Actualizamos los límites
    if fxl * fxr < 0:
      xu = xr
    elif fxl * fxr > 0:
      xl = xr
    elif fxl * fxr == 0:
      st.success(f"La raíz está en: ({round(xr,4)}, {round(fxr,4)})")
      break

    xr_ant = xr
    it += 1

    # Mostrar la figura en el espacio reservado
    fig_placeholder.pyplot(fig)
    tablita.dataframe(tabla)
    # Borra la figura para la siguiente iteración
    plt.close(fig)

def newtonRaphsonMethod(func, xi, tol, start_range, end_range, var):
   # Tolerancia y valores iniciales
  global x
  error = tol + 1
  it = 1
  x = sp.symbols(var)
  y = sp.sympify(func)

  # Dataframe para almacenar los resultados
  columnas = ['xi','Xi+1','f(xi)',"f'(Xi)",'er(%)']
  tabla = pd.DataFrame(columns=columnas)

  # Espacio reservado para la figura
  fig_placeholder = st.empty()
  tablita = st.empty()
  fig_placeholder.markdown(
    """
    <style>
    div[data-testid="stBlock"] {
        width: 200px;
    }
    </style>
    """, unsafe_allow_html=True)
  while error > tol:
    fxi = y.subs({x: xi}).evalf()

    # Crear la figura
    fig, ax = plt.subplots()
    r = np.linspace(start_range, end_range, 100)
    fx = calculate_y(r, y)

    ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
    ax.vlines(x=0, ymin=min(fx)-0.5, ymax=max(fx)+0.5, color='k')
    ax.hlines(y=0, xmin=min(r)-0.5, xmax=max(r)+0.5, color='k')
    ax.set_title(f"${sp.latex(y)}$")
    ax.grid()

    # Límites xl y xu
    ax.vlines(x=0, ymin=min(fx)-0.1, ymax=fxi, color='k', linestyle='--', label=f'$x_l=${xi}')
    ax.hlines(y=0, xmin=min(r)-0.1, xmax=max(r)+0.1,color='k')

    ## Punto inicial
    ax.plot([xi],[fxi], color='red', marker='o', label=f'$(x_{it},f(x_{it}))= ({xi},{fxi})$')

    ## Calculemos la derivada
    dy = y.diff()
    ## Evaluemos la derivada en x_i
    dfxi = dy.subs({x:xi}).evalf()

    ## Calculemos el x_i+1 (siguiente)
    xs = round(xi - ((fxi)/(dfxi)),4)
    ax.plot([xs],[0], color='red', marker='x', label=f'$(x_{it+1},0) = ({xs},0)$')

    h=0.1
    dfx = (y.subs({x:xi+h})-y.subs({x:xi}))/h # derivative
    tan = y.subs({x:xi})+dfx*(r-xi)  # tangent
    ax.plot(r,tan,color='purple',linestyle='--',label=f"${sp.latex(dy)}$")

    error = np.abs((xs - xi)/ xs) * 100 if xs != 0 else 0
    # error = np.abs((xr - xr_ant) / xr) * 100 if xr != 0 else 0
    nueva_fila = {'xi':xi,'Xi+1':xs,'f(xi)':fxi,"f'(Xi)":dfxi,'er(%)':round(error,4)}
    tabla = pd.concat([tabla, pd.DataFrame([nueva_fila])], ignore_index=True)

    it += 1
    xi = xs

    # Mostrar la figura en el espacio reservado
    fig_placeholder.pyplot(fig)
    tablita.dataframe(tabla)
    # Borra la figura para la siguiente iteración
    plt.close(fig)

def secantMethod(func, xl, xu, tol, start_range, end_range, var):
  # Tolerancia y valores iniciales
  global x
  xr = None
  xr_ant = xu
  error = tol + 1
  it = 1
  x = sp.symbols(var)
  y = sp.sympify(func)

  # Dataframe para almacenar los resultados
  columnas = ['Xl', 'Xu', 'Xr', 'er(%)', 'f(Xl)', 'f(Xu)', 'f(Xr)']
  tabla = pd.DataFrame(columns=columnas)

  # Espacio reservado para la figura
  fig_placeholder = st.empty()
  tablita = st.empty()
  fig_placeholder.markdown(
    """
    <style>
    div[data-testid="stBlock"] {
        width: 200px;
    }
    </style>
    """, unsafe_allow_html=True)
  
  while error > tol:
    # Evaluamos la función en los puntos del intervalo
    fxl = y.subs({x: xl}).evalf()
    fxu = y.subs({x: xu}).evalf()

    # Crear la figura
    fig, ax = plt.subplots()
    r = np.linspace(start_range, end_range, 100)
    fx = calculate_y(r, y)

    ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
    ax.vlines(x=0, ymin=min(fx)-0.5, ymax=max(fx)+0.5, color='k')
    ax.hlines(y=0, xmin=min(r)-0.5, xmax=max(r)+0.5, color='k')
    ax.set_title(f"${sp.latex(y)}$")
    ax.grid()

    # Límites xl y xu
    ax.vlines(x=xl, ymin=0, ymax=fxl, color='k', linestyle='--', label=f'$x_l=${xl}')
    ax.vlines(x=xu, ymin=0, ymax=fxu, color='k', linestyle='--', label=f'$x_u=${xu}')

    # Calculamos la raíz
    xr = round((xl * fxu - xu * fxl) / (fxu - fxl), 4)
    fxr = y.subs({x: xr}).evalf()

    # Pintamos el punto intermedio
    ax.plot(xr, fxr, 'ro', label=f'Raíz={xr}')
    ax.legend()

    # Actualizamos el error y la tabla
    error = np.abs((xr - xr_ant) / xr) * 100 if xr != 0 else 0
    nueva_fila = {'Xl': xl, 'Xu': xu, 'Xr': xr, 'er(%)': error, 'f(Xl)': fxl, 'f(Xu)': fxu, 'f(Xr)': fxr}
    tabla = pd.concat([tabla, pd.DataFrame([nueva_fila])], ignore_index=True)

    if fxl * fxr < 0:
      xu = xr
    elif fxl * fxr > 0:
      xl = xr
    elif fxl * fxr == 0:
      st.success(f"La raíz está en: ({round(xr,4)}, {round(fxr,4)})")
      break

    xr_ant = xr
    it += 1

    # Mostrar la figura en el espacio reservado
    fig_placeholder.pyplot(fig)
    tablita.dataframe(tabla)
    # Borra la figura para la siguiente iteración
    plt.close(fig)

def variantSecantMethod(func, xl, xu, tol, start_range, end_range, var, max_iteration):
  # Tolerancia y valores iniciales
  global x
  xr = None
  it = 0
  x = sp.symbols(var)
  y = sp.sympify(func)

  # Dataframe para almacenar los resultados
  columnas = ['Iteración', 'Xn', 'f(Xn)']
  tabla = pd.DataFrame(columns=columnas)

  # Espacio reservado para la figura
  fig_placeholder = st.empty()
  tablita = st.empty()
  fig_placeholder.markdown(
    """
    <style>
    div[data-testid="stBlock"] {
        width: 200px;
    }
    </style>
    """, unsafe_allow_html=True)
  
  while it < max_iteration:
    # Evaluamos la función en los puntos del intervalo
    fxl = y.subs({x: xl}).evalf()
    fxu = y.subs({x: xu}).evalf()

    # Crear la figura
    fig, ax = plt.subplots()
    r = np.linspace(start_range, end_range, 100)
    fx = calculate_y(r, y)

    ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
    ax.vlines(x=0, ymin=min(fx)-0.5, ymax=max(fx)+0.5, color='k')
    ax.hlines(y=0, xmin=min(r)-0.5, xmax=max(r)+0.5, color='k')
    ax.set_title(f"${sp.latex(y)}$")
    ax.grid()

    # Límites xl y xu
    ax.vlines(x=xl, ymin=0, ymax=fxl, color='k', linestyle='--', label=f'$x_l=${xl}')
    ax.vlines(x=xu, ymin=0, ymax=fxu, color='k', linestyle='--', label=f'$x_u=${xu}')

    xr = round(xu - (fxu * (xu - xl)) / (fxu - fxl), 4)
    fxr = y.subs({x: xr}).evalf()

    # Pintamos el punto intermedio
    ax.plot(xr, fxr, 'ro', label=f'Raíz={xr}')
    ax.legend()

    # Actualizamos el error y la tabla
    # error = np.abs((xr - xr_ant) / xr) * 100 if xr != 0 else 0
    nueva_fila = {'Iteración': it, 'Xn': xr, 'f(Xn)': fxr}
    tabla = pd.concat([tabla, pd.DataFrame([nueva_fila])], ignore_index=True)

    # Mostrar la figura en el espacio reservado
    fig_placeholder.pyplot(fig)
    tablita.dataframe(tabla)
    # Borra la figura para la siguiente iteración
    plt.close(fig)

    # Verificar convergencia
    if abs(fxr) < tol:
      st.success(f"La raíz está en la iteración {it}: ({round(xr,4)}, {round(fxr,4)})")
      break

    xl = xu
    xu = xr
    fxl = fxu
    fxu = fxr
    it += 1

def fixedPoint(func, xl, xu, tol, start_range, end_range, var, max_iteration, initial_value):
  # Tolerancia y valores iniciales
  global x
  xr = None
  it = 1
  x = sp.symbols(var)
  y = sp.sympify(func)
  f = sp.lambdify(x, y)

  # Dataframe para almacenar los resultados
  columnas = ['Iteración', 'Xn', 'f(Xn)']
  tabla = pd.DataFrame(columns=columnas)

  # Espacio reservado para la figura
  fig_placeholder = st.empty()
  tablita = st.empty()
  fig_placeholder.markdown(
    """
    <style>
    div[data-testid="stBlock"] {
        width: 200px;
    }
    </style>
    """, unsafe_allow_html=True)
  
  while it < max_iteration:
    # Evaluamos la función en los puntos del intervalo
    fxl = y.subs({x: xl}).evalf()
    fxu = y.subs({x: xu}).evalf()

    # Crear la figura
    fig, ax = plt.subplots()
    r = np.linspace(start_range, end_range, 100)
    fx = calculate_y(r, y)

    ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
    ax.vlines(x=0, ymin=min(fx)-0.5, ymax=max(fx)+0.5, color='k')
    ax.hlines(y=0, xmin=min(r)-0.5, xmax=max(r)+0.5, color='k')
    ax.set_title(f"${sp.latex(y)}$")
    ax.grid()

    # Límites xl y xu
    ax.vlines(x=xl, ymin=0, ymax=fxl, color='k', linestyle='--', label=f'$x_l=${xl}')
    ax.vlines(x=xu, ymin=0, ymax=fxu, color='k', linestyle='--', label=f'$x_u=${xu}')

    # Calcular la siguiente aproximación
    xr = round(f(initial_value),4)
    fxr = y.subs({x: xr}).evalf()
    # Calculamos la raíz
    # xr = round((xl + xu) / 2, 4)
    # Pintamos el punto intermedio
    ax.plot(xr, fxr, 'ro', label=f'Raíz={xr}')
    ax.legend()

    # Actualizamos el error y la tabla
    nueva_fila = {'Iteración': it, 'Xn': x, 'f(Xn)': fxr}
    tabla = pd.concat([tabla, pd.DataFrame([nueva_fila])], ignore_index=True)

    # Mostrar la figura en el espacio reservado
    fig_placeholder.pyplot(fig)
    tablita.dataframe(tabla)
    # Borra la figura para la siguiente iteración
    plt.close(fig)

    # Verificar convergencia
    if abs(fxr) < tol:
      st.success(f"La raíz está en la iteración {it}: ({round(xr,4)}, {round(fxr,4)})")
      break

    xl = xu
    xu = xr
    fxl = fxu
    fxu = fxr
    it += 1

class RootCalculation:
    def __init__(self):
        print("Esto es el init")