import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

## ----- Runge Kutta 3 
# Definición de las funciones para el sistema de ecuaciones diferenciales de prueba
def func_i(v, i, t):
    return 1 - i - v

def func_v(i, v, t):
    return i

def e1(t):
    # Función analítica de ejemplo para la variable i(t)
    return np.sin(t)

def e2(t):
    # Función analítica de ejemplo para la variable v(t)
    return np.cos(t)

def runge_kutta_3_system(funcs, y0, t_range, dt):
    t_values = np.arange(t_range[0], t_range[1], dt)
    y_values = [np.array(y0)]

    for t in t_values[:-1]:
        y_current = y_values[-1]

        k1 = np.array([f(*y_current, t) for f in funcs])
        k2 = np.array([f(*(y_current + k1 * dt/2), t + dt/2) for f in funcs])
        k3 = np.array([f(*(y_current + k2 * dt), t + dt) for f in funcs])  # Corrección aquí

        y_next = y_current + dt * (1/6 * k1 + 2/3 * k2 + 1/6 * k3)
        y_values.append(y_next)

    return t_values, np.array(y_values).T

def rungeKutta3(initial_i, initial_v, tr):
    dt = 0.1 # Paso del tiempo
    initial_conditions = [initial_i, initial_v]
    time_range = (0, tr)

    t_values_rk3, [i_values_rk3_system, v_values_rk3_system] = runge_kutta_3_system(
        [func_i, func_v], initial_conditions, time_range, dt)
    
    # Rango de valores de tiempo para las funciones analíticas
    t_vals = np.arange(time_range[0], time_range[1], dt)
    
    fig_placeholder_i = st.empty() # Espacio reservado para la figura
    fig_placeholder_v = st.empty() # Espacio reservado para la figura
    
    plt.figure(figsize=(10, 6))
    fig, ax = plt.subplots()
    plt.plot(t_vals, e1(t_vals), label='Analítico i(t)')
    plt.plot(t_values_rk3, i_values_rk3_system, label='RK3 Aproximado i(t)', linestyle='-.')
    plt.xlabel('Tiempo')
    plt.ylabel('Corriente (i(t))')
    plt.title('Corriente en función del tiempo')
    plt.grid(True)
    plt.legend()
    fig_placeholder_i.pyplot(fig)

    fig1, ax = plt.subplots()
    plt.plot(t_vals, e2(t_vals), label='Analítico v(t)', color='orange')
    plt.plot(t_values_rk3, v_values_rk3_system, label='RK3 Aproximado v(t)', linestyle='-.', color='purple')
    plt.xlabel('Tiempo')
    plt.ylabel('Voltaje (v(t))')
    plt.title('Voltaje en función del tiempo')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    
    fig_placeholder_v.pyplot(fig1)
    plt.close(fig)
    plt.close(fig1)

## ----- Runge Kutta 4 
def func_i(i, v, t):
    # Ejemplo: Ecuación diferencial para la corriente i
    R = 1.0  # Resistencia
    L = 0.5  # Inductancia
    V = 1.0  # Voltaje de la fuente
    return (V - R * i) / L

def func4_v(i, v, t):
    # Ejemplo: Ecuación diferencial para el voltaje v
    C = 1.0  # Capacidad
    return i / C

def runge_kutta_4_system(funcs, y0, t_range, dt):
    """
    Método de Runge-Kutta de orden 4 para un sistema de ecuaciones diferenciales.
    :param funcs: Lista de funciones que representan el sistema de ecuaciones diferenciales.
    :param y0: Condiciones iniciales para cada variable en el sistema.
    :param t_range: Rango de tiempo como una tupla (inicio, fin).
    :param dt: Paso de tiempo.
    :return: Tupla de listas (tiempos, valores de cada variable).
    """
    t_values = np.arange(t_range[0], t_range[1], dt)
    y_values = [np.array(y0)]

    for t in t_values[:-1]:
        y_current = y_values[-1]

        k1 = np.array([f(*y_current, t) for f in funcs])
        k2 = np.array([f(*(y_current + k1 * dt/2), t + dt/2) for f in funcs])
        k3 = np.array([f(*(y_current + k2 * dt/2), t + dt/2) for f in funcs])
        k4 = np.array([f(*(y_current + k3 * dt), t + dt) for f in funcs])

        y_next = y_current + dt * (1/6 * k1 + 1/3 * k2 + 1/3 * k3 + 1/6 * k4)
        y_values.append(y_next)

    return t_values, np.array(y_values).T

def rungeKutta4(initial_i, initial_v, tr, r, c, i, v):
    dt = 0.1 # Paso del tiempo
    initial_conditions = [initial_i, initial_v]
    time_range = (0, tr)

    t_values_rk4, [i_values_rk4_system, v_values_rk4_system] = runge_kutta_4_system(
    [func_i, func_v], initial_conditions, time_range, dt)
    
    fig_placeholder_i = st.empty() # Espacio reservado para la figura
    fig_placeholder_v = st.empty() # Espacio reservado para la figura
    fig_placeholder_d = st.empty() # Espacio reservado para la figura
    
    plt.figure(figsize=(10, 6))
    fig, ax = plt.subplots()
    plt.plot(t_values_rk4, e1(t_values_rk4), label='Analítico i(t)')
    plt.plot(t_values_rk4, i_values_rk4_system, label='RK4 Aproximado i(t)', linestyle=':')
    plt.xlabel('Tiempo')
    plt.ylabel('Corriente (i(t))')
    plt.title('Corriente en función del tiempo')
    plt.grid(True)
    plt.legend()
    fig_placeholder_i.pyplot(fig)

    fig1, ax = plt.subplots()
    plt.plot(t_values_rk4, e2(t_values_rk4), label='Analítico v(t)', color='orange')
    plt.plot(t_values_rk4, v_values_rk4_system, label='RK4 Aproximado v(t)', linestyle=':', color='green')
    plt.xlabel('Tiempo')
    plt.ylabel('Voltaje (v(t))')
    plt.title('Voltaje en función del tiempo')
    plt.grid(True)
    plt.legend()

    fig_placeholder_v.pyplot(fig1)

    fig2, ax = plt.subplots()
    plt.plot(i_values_rk4_system, v_values_rk4_system, label='RK4 Fases', linestyle=':', color='red')
    plt.xlabel('Corriente (i(t))')
    plt.ylabel('Voltaje (v(t))')
    plt.title('Diagrama de fases')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    
    fig_placeholder_d.pyplot(fig2)
    plt.close(fig)
    plt.close(fig1)
    plt.close(fig2)

## ----- Depredador Presa
# Definir las ecuaciones del modelo Lotka-Volterra
def lotka_volterra(t, X, alpha, beta, gamma, delta):
    x, y = X
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return np.array([dxdt, dydt])

# Implementar el método de Runge-Kutta de segundo orden
def runge_kutta2(f, t0, x0, h, t_max, *args):
    t_values = [t0]
    x_values = [x0]

    while t0 < t_max:
        k1 = h * f(t0, x0, *args)
        k2 = h * f(t0 + h, x0 + k1, *args)
        x0 = x0 + 0.5 * (k1 + k2)
        t0 += h

        t_values.append(t0)
        x_values.append(x0)

    return np.array(t_values), np.array(x_values)

def predatorPrey(x0, y0, alpha, beta, gamma, delta, h, t0, t_max):
    fig_placeholder = st.empty() # Espacio reservado para la figura
    initial_conditions = np.array([x0, y0])
    t, populations = runge_kutta2(lotka_volterra, t0, initial_conditions, h, t_max, alpha, beta, gamma, delta)

    plt.figure(figsize=(10, 6))
    fig, ax = plt.subplots()
    plt.plot(t, populations[:, 0], label='Presas (x)')
    plt.plot(t, populations[:, 1], label='Depredadores (y)')
    plt.xlabel('Tiempo')
    plt.ylabel('Población')
    plt.title('Modelo de Lotka-Volterra')
    plt.legend()
    plt.grid(True)
    fig_placeholder.pyplot(fig)
    # Borra la figura para la siguiente iteración
    plt.close(fig)
