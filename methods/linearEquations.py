import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import ast

def convertMatrizOrVector(elem, isMatriz):
    try:
        return ast.literal_eval(elem)
    except (SyntaxError, ValueError):
        st.error(f'Ingrese un {"a matriz" if isMatriz else " vector"} con el formato adecuado.')

def gaussiana(matriz, vector, solution):
    matriz = convertMatrizOrVector(matriz, True)
    vector = convertMatrizOrVector(vector, False)
    if len(solution) > 0:
        solution = convertMatrizOrVector(solution, False)

    A = np.array(matriz, dtype=float)
    b = np.array(vector, dtype=float)
    error = 0.0
    fig_placeholder = st.empty() # Espacio reservado para la figura

    n = len(b)
    x = np.zeros(n)

    for i in range(n):
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            b[j] -= factor * b[i]
            A[j, i:] -= factor * A[i, i:]

    # Resolver el sistema lineal escalonado mediante sustitución hacia adelante
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.sum(A[i, i+1:] * x[i+1:])) / A[i, i]
    
    # Cálculo del error (comparando con una solución conocida)
    if len(solution) > 0:
        sol = np.array(solution, dtype=float)
        error = np.linalg.norm(sol - x)  # Error norma euclidiana

    # Gráfica
    plt.plot(x, 'bo-', label='Solución')
    plt.title('Eliminación Gaussiana')
    if len(solution) > 0:
        plt.plot(sol, 'go--', label='Solución Conocida')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid()

    st.warning(f'Error: {error:.2f}%')
    fig_placeholder.pyplot(plt)

def linealTriangular(matriz, vector, solution):
    matriz = convertMatrizOrVector(matriz, True)
    vector = convertMatrizOrVector(vector, False)
    if len(solution) > 0:
        solution = convertMatrizOrVector(solution, False)

    U = np.array(matriz)
    b = np.array(vector)
    error = 0.0
    fig_placeholder = st.empty() # Espacio reservado para la figura
    n = len(b)
    x = np.zeros(n)

    # Resolución del sistema lineal mediante sustitución hacia atrás
    for i in range(n-1, -1, -1):
        suma = sum(U[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - suma) / U[i][i]

    # Cálculo del error (comparando con una solución conocida)
    if len(solution) > 0:
        sol = np.array(solution)
        error = np.linalg.norm(sol - x)  # Error norma euclidiana

    plt.plot(x, 'bo-', label='Solución')
    if len(solution) > 0:
        plt.plot(sol, 'go--', label='Solución Conocida')
    plt.title('Sistema Lineal Triangular')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid()

    st.warning(f'Error: {error:.2f}%')
    fig_placeholder.pyplot(plt)

def pivot(matriz, vector, solution):
    matriz = convertMatrizOrVector(matriz, True)
    vector = convertMatrizOrVector(vector, False)
    if len(solution) > 0:
        solution = convertMatrizOrVector(solution, False)

    A = np.array(matriz, dtype=float)
    b = np.array(vector, dtype=float)
    error = 0.0
    fig_placeholder = st.empty() # Espacio reservado para la figura

    n = len(b)
    x = np.zeros(n)

    for i in range(n):
        # Seleccionar la fila con el máximo valor en la columna actual
        max_row = np.argmax(abs(A[i:, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            b[j] -= factor * b[i]
            A[j, i:] -= factor * A[i, i:]

    # Resolver el sistema lineal escalonado mediante sustitución hacia adelante
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.sum(A[i, i+1:] * x[i+1:])) / A[i, i]

    # Cálculo del error (comparando con una solución conocida)
    if len(solution) > 0:
        sol = np.array(solution, dtype=float)
        error = np.linalg.norm(sol - x)  # Error norma euclidiana

    plt.plot(x, 'bo-', label='Solución')
    if len(solution) > 0:
        plt.plot(sol, 'go--', label='Solución Conocida')
    plt.title('S.L.R (Pivoteo)')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid()

    st.warning(f'Error: {error:.2f}%')
    fig_placeholder.pyplot(plt)