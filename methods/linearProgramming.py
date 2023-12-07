import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog
import streamlit as st
import sympy as sp
import ast
from scipy.spatial import ConvexHull

#---- Método Gráfico

def convertVector(elem):
    try:
        return ast.literal_eval(elem)
    except (SyntaxError, ValueError):
        st.error(f'Ingrese un vector con el formato adecuado.')

def graphicalMethod(func, restricciones, variables):
    restricciones = convertVector(restricciones)
    variables = convertVector(variables)
     # Crear el gráfico
    x_vals = np.linspace(0, 30, 400)
    plt.figure(figsize=(8, 6))
    fig_placeholder = st.empty()
    fig, ax = plt.subplots()
    
    # Convertir variables a símbolos de sympy
    x, y = sp.symbols(variables[0]), sp.symbols(variables[1])
    
    # Graficar restricciones
    for restriccion in restricciones:
        expr = sp.sympify(restriccion)
        y_vals = np.array([sp.solve(expr.subs(x, val), y) for val in x_vals])
        plt.plot(x_vals, y_vals, label=restriccion)

    # Encontrar la región factible
    region_factible = np.zeros(len(x_vals), dtype=bool)
    for restriccion in restricciones:
        expr = sp.sympify(restriccion)
        for idx, val in enumerate(x_vals):
            if expr.subs(x, val).is_nonpositive:
                region_factible[idx] = True

    plt.fill_between(x_vals, 0, 30, where=region_factible, alpha=0.2)
    
    # Restricciones positivas
    plt.xlim((0, 30))
    plt.ylim((0, 30))
    plt.xlabel(variables[0])
    plt.ylabel(variables[1])
    plt.legend()
    plt.grid()
    plt.show()

    # Vértices de la región factible (simulados para este ejemplo)
    vertices_x = [0, 8, 0]
    vertices_y = [10, 4, 0]

    # Evaluar la función objetivo en los vértices
    funcion_evaluada = [sp.sympify(func).subs({x: val_x, y: val_y}) for val_x, val_y in zip(vertices_x, vertices_y)]

    # Encontrar el índice del vértice que maximiza la función objetivo
    indice_max = np.argmax(funcion_evaluada)
    x_max, y_max = vertices_x[indice_max], vertices_y[indice_max]

    st.success(f"El máximo valor de la función objetivo es {funcion_evaluada[indice_max]} en (x={x_max}, y={y_max})")
    fig_placeholder.pyplot(fig)
    plt.close(fig)


#---- Método Simplex
def plot_feasible_region(vertices):
    hull = ConvexHull(vertices)
    plt.plot(np.append(hull.points[hull.vertices, 0], hull.points[hull.vertices, 0][0]),
             np.append(hull.points[hull.vertices, 1], hull.points[hull.vertices, 1][0]),
             'k-')
    
def plot_constraints(coefficients, constants, sign):
    x_vals = np.linspace(0, 10, 100)
    for i in range(len(coefficients)):
        if sign[i] == '<=':
            plt.plot(x_vals, (constants[i] - coefficients[i, 0] * x_vals) / coefficients[i, 1], label=f'{coefficients[i, 0]}x + {coefficients[i, 1]}y <= {constants[i]}')
        elif sign[i] == '>=':
            plt.plot(x_vals, (constants[i] - coefficients[i, 0] * x_vals) / coefficients[i, 1], label=f'{coefficients[i, 0]}x + {coefficients[i, 1]}y >= {constants[i]}')
        elif sign[i] == '==':
            plt.plot(x_vals, (constants[i] - coefficients[i, 0] * x_vals) / coefficients[i, 1], label=f'{coefficients[i, 0]}x + {coefficients[i, 1]}y = {constants[i]}')


def simplexMethod(v, c, ct, s):
    vertices = np.array([list(map(float, coord.split())) for coord in v.split(',')])
    coefficients = np.array([list(map(float, coef.split())) for coef in c.split(',')])
    constants = np.array(list(map(float, ct.split())))
    fig_placeholder = st.empty()
    fig, ax = plt.subplots()

    # Graficar las restricciones y la región factible
    plot_constraints(coefficients, constants, s)
    plot_feasible_region(vertices)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Graphical Method for Linear Programming')
    plt.legend()
    plt.grid(True)

    fig_placeholder.pyplot(fig)
    plt.close(fig)