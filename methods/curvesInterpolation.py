import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
from scipy.interpolate import CubicSpline
from sklearn.metrics import r2_score, mean_squared_error

def smallSquares(data_file):
    data = pd.read_csv(data_file)
    df = pd.DataFrame(data)

    # Espacio reservado para la figura
    fig_normi_placeholder = st.empty() # plot normal
    fig_alter_placeholder = st.empty() # plot con ajuste

    fig, ax = plt.subplots()

    ax.scatter(df["X"].to_list(),df["Y"].to_list(),color='blue',label="datos")
    ax.set_title("Regresión")
    ax.grid()
    ax.legend()
    plt.show()

    # Calculamos las sumatorias y la pendiente y el intercepto de la recta.
    x = np.array(df["X"])
    y = np.array(df["Y"])

    sx = np.sum(x)
    sy = np.sum(y)

    sx2 = np.sum(x**2)
    sxy = np.sum(x*y)

    n = len(x)

    m = ((n*sxy) - (sx*sy))/((n*sx2)-(sx**2))
    b = (sy -(m*sx))/n

    st.success(f"Pendiente: ({m}) - Intercepto: ({b})")
    
    fig_regression, axR = plt.subplots()
    # Verificar como se realizó la interpolación
    recta = m*x + b

    axR.scatter(df["X"].to_list(),df["Y"].to_list(),color='blue',label="datos")
    axR.plot(x,recta,color='red',label="y=mx+b")

    # Calcular R^2
    r2 = r2_score(y, recta)
    # print(f"R^2: {r2}")
    axR.text(60, -0.6, f"$R^2: {r2}$", fontsize=9, color='black')
    # Calcular MSE
    mse = mean_squared_error(y, recta)
    axR.text(60, -0.67, f"$mse: {mse}$", fontsize=9, color='black')
    # print(f"mse: {mse}")

    axR.set_title("Regresión")
    axR.grid()
    axR.legend()
    plt.show()

    # Mostrar la figura en el espacio reservado
    fig_normi_placeholder.pyplot(fig)
    fig_alter_placeholder.pyplot(fig_regression)
    plt.close(fig)

def lagrange(data_file):
    data = pd.read_csv(data_file)
    df = pd.DataFrame(data)
    fig_placeholder = st.empty() # plot normal

    x = sp.symbols('x')
    
    xi = np.array(df["x"])
    fi = np.array(df["y"])

    polinomio = 0
    for i in range(len(xi)):
        num = 1
        deno = 1
        for j in range(len(xi)):
            if j != i:
                num *= (x-xi[j])
                deno *= (xi[i]-xi[j])
        res = num/deno
        polinomio += res*fi[i]

    simply = polinomio.expand()
    px = sp.lambdify(x,simply)
    muestras = 100
    a,b = min(xi),max(xi)
    pxi = np.linspace(a,b,muestras)
    pfi = px(pxi)
    
    plt.subplots(figsize=(10,8))
    plt.plot(xi, fi, 'o', label='Puntos')
    plt.plot(pxi, pfi, label='Polinomio')
    plt.title('Interpolación Lagrange')
    # plt.text(0, 3.0,f' Polinomio: ${sp.latex(polinomio)}$', fontsize=10, color='black')
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.grid(1)
    plt.legend()
    st.success(f' Polinomio: ${sp.latex(polinomio)}$')
    fig_placeholder.pyplot(plt)

def splinesCubics(data_file):
    data = pd.read_csv(data_file)
    df = pd.DataFrame(data)
    fig_placeholder = st.empty() # plot normal

    x = np.array(df["x"])
    y = np.array(df["y"])

    # Calcula la spline cúbica
    cs = CubicSpline(x, y)

    x_new = np.linspace(0, 5, 100)

    x_interp = 2.5 # Punto de interpolación
    y_new = cs(x_new)

    y_interp = cs(x_interp)

    plt.figure()
    plt.scatter(x, y, label='Datos Originales', color='blue')
    plt.plot(x_new, y_new, label='Spline Cúbica', color='red')
    # plt.text(0, -5, f'Interpolado: ({x_interp}, {y_interp})', fontsize=9, color='black')
    plt.legend()
    plt.title('Spline Cúbica')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

    st.success(f'Interpolado: ({x_interp}, {y_interp})')
    fig_placeholder.pyplot(plt)

def polynomialRegression(data_file):
    data = pd.read_csv(data_file)
    df = pd.DataFrame(data)
    fig_placeholder = st.empty() # plot normal

    x = np.array(df["x"])
    y = np.array(df["y"])

    degree = 2
    coefficients = np.polyfit(x, y, degree)

    # Crear un polinomio a partir de los coeficientes
    polynomial = np.poly1d(coefficients)

    x_new = np.linspace(0, 7, 100)
    y_new = polynomial(x_new)

    x_interp = 2.5  # # Punto de interpolación
    y_interp = polynomial(x_interp)

    # Graficar los datos originales y la regresión polinomial
    plt.scatter(x, y, label='Datos Originales', color='blue')
    plt.plot(x_new, y_new, label=f'Regresión Polinomial (grado {degree})', color='green')
    plt.title('Regresión Polinomial')
    plt.xlabel('x')
    plt.ylabel('y')
    # plt.text(0, -15, f'Interpolado: ({x_interp}, {y_interp:2f})', fontsize=9, color='black')
    plt.legend()
    plt.grid()
    # plt.show()
    st.success(f'Interpolado: ({x_interp}, {y_interp:2f})')
    fig_placeholder.pyplot(plt)