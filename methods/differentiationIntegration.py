import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import streamlit as st

def calculate_y(x_values, expression):
  return [expression.subs({x: xi}) for xi in x_values]

def eulerMethod(var, func, ti, tf, h, y0):
    t = sp.symbols(var)
    dy = sp.sympify(func)

    # Dataframe para almacenar los resultados
    columnas =  ['it','t','yi','yi+1']
    tabla = pd.DataFrame(columns=columnas)

    x = np.arange(ti, tf + h, h)
    y = np.empty_like(x)

    fig_placeholder = st.empty() # Espacio reservado para la figura
    tablita = st.empty()

    for i in range(0,len(y)-1):
        y[i+1] = y[i] + h * dy.subs({t:x[i]})
        nueva_fila = pd.DataFrame(data={'it':[i+1],'t':[round(x[i],2)],'yi':[round(y[i],2)],'yi+1':[round(y[i+1],2)]})
        tabla = pd.concat([tabla,nueva_fila], ignore_index=True)

    plt.figure()
    fig, ax = plt.subplots()
    ax.grid()
    ax.plot(x,y, marker='o', label = 'Método Euler')
    ax.plot(x, [sp.integrate(dy).subs({t:i}) for i in x], label='Real')
    ax.legend()

    # Mostrar la figura en el espacio reservado
    fig_placeholder.pyplot(fig)
    tablita.dataframe(tabla)
    # Borra la figura para la siguiente iteración
    plt.close(fig)
    
def trapezoid(var, func, a, b, start_range, end_range):
    global x
    x = sp.symbols(var)
    y = sp.sympify(func)

    fli = y.subs({x: a}).evalf()
    fls = y.subs({x: b}).evalf()

    # Regla trapezoidal
    I = (b-a) * ((fli+fls)/2)
    # Error
    e = np.abs((2.333 - I)/(2.333)) * 100

    fig_placeholder = st.empty()

    # Crear la figura
    fig, ax = plt.subplots()
    r = np.linspace(start_range, end_range, 100)
    fx = calculate_y(r, y)

    ax.set_title('${}$'.format(sp.latex(y)))
    ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
    ax.vlines(x=0, ymin=min(fx)-0.5, ymax=max(fx)+0.5, color='k')
    ax.hlines(y=0, xmin=min(r)-0.5, xmax=max(r)+0.5, color='k')
    ax.grid(True)

    # Límites xl y xu
    ax.vlines(x=0, ymin=min(fx), ymax=max(fx), color='k')
    ax.hlines(y=0, xmin=min(r), xmax=max(r), color='k')

    ax.vlines(x=a, ymin=0, ymax=fli, color='r', linestyle='--')
    ax.vlines(x=b, ymin=0, ymax=fls, color='r', linestyle='--')
    ax.plot([a, b], [fli, fls], color='r', linestyle='--')

    ax.fill([a, a, b, b], [0, fli, fls, 0], 'r', alpha=0.2)

    ax.set_title('Trapezoide')
    plt.grid(True)
    plt.legend()

    st.warning('Error: '+str(round(e,2))+'%')
    fig_placeholder.pyplot(fig)

def multipleTrapezoid(var, func, a, b, start_range, end_range, n):
    global x
    x = sp.symbols(var)
    y = sp.sympify(func)
    a = sp.sympify(a)
    b = sp.sympify(b)
    n = sp.sympify(n)
    h = sp.S((b - a) / n)

    plt.figure()
    t = np.arange(a,b+h,h)
    sum = 0.0
    for i in range(1, len(t)-1):
        sum += y.subs({x:t[i]}).evalf()

    I = h/2*(y.subs({x:t[0]})+2*sum+y.subs({x:t[-1]}))
    I_real = sp.integrate(y,(x,a,b))

    fig_placeholder = st.empty()
    error = np.abs((I_real - I)/(I_real))*100

    fig, ax = plt.subplots()
    r = np.linspace(start_range, end_range, 100)
    fx = calculate_y(r, y)

    ax.set_title('${}$'.format(sp.latex(y)))
    ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
    ax.vlines(x=0, ymin=min(fx)-0.5, ymax=max(fx)+0.5, color='k')
    ax.hlines(y=0, xmin=min(r)-0.5, xmax=max(r)+0.5, color='k')
    ax.grid(True)

    # Límites xl y xu
    ax.vlines(x=0, ymin=min(fx), ymax=max(fx), color='k')
    ax.hlines(y=0, xmin=min(r), xmax=max(r), color='k')

    fa = y.subs({x:a}).evalf()
    fb = y.subs({x:b}).evalf()

    ax.vlines(x=a, ymin=0, ymax=fa, color='r', linestyle='--')
    ax.vlines(x=b, ymin=0, ymax=fb, color='r', linestyle='--')

    color = ['r','g','b','y','blueviolet', 'darkcyan','#A9A9A9','darkorange']

    for i in range(0, len(t)):
        fa = y.subs({x: t[i]}).evalf()
        fb = y.subs({x: t[i]+h}).evalf()
        ax.vlines(x= t[i], ymin= 0, ymax= y.subs({x: t[i]}), color= 'r', linestyle='--')
        x0 = t[i]; x1 = t[i+1] if i+1 < len(t) else t[i]
        ax.fill([x0,x0, x1, x1],[0,fa,y.subs({x:t[i]+h}),0], random.choice(color), alpha=0.2)
        if i+1 < len(t):
            ax.plot([x0,x0+h],[fa,fb], color='r', linestyle='--')
    
    ax.set_title('Trapezoide')
    plt.grid(True)
    plt.legend()

    st.warning('Error: '+str(round(error,2))+'%')
    fig_placeholder.pyplot(fig)

def simpson1_3(var, func, a, b, start_range, end_range):
    global x
    x = sp.symbols(var)
    m = (a + b) / 2
    y = sp.sympify(func)

    fa = y.subs({x: a}).evalf()
    fb = y.subs({x: b}).evalf()
    fm = y.subs({x: m}).evalf()

    fig_placeholder = st.empty() # Espacio reservado para la figura
    # Aplicamos la regla de Simpson 1/3
    I = (b - a) * ((fa + 4 * fm + fb) / 6)

    # Ahora usemos la función de integración simbólica de sympy
    I_real = sp.integrate(y, (x, a, b))

    error = np.abs((I_real - I) / (I_real)) * 100

    # Crear la figura
    fig, ax = plt.subplots()
    r = np.linspace(start_range, end_range, 100)
    fx = calculate_y(r, y)

    ax.set_title('${}$'.format(sp.latex(y)))
    ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
    ax.vlines(x=0, ymin=min(fx)-0.5, ymax=max(fx)+0.5, color='k')
    ax.hlines(y=0, xmin=min(r)-0.5, xmax=max(r)+0.5, color='k')
    ax.grid(True)

    # Límites xl y xu
    ax.vlines(x=0, ymin=min(fx), ymax=max(fx), color='k')
    ax.hlines(y=0, xmin=min(r), xmax=max(r), color='k')

    ax.vlines(x=a, ymin=0, ymax=fa, color='r', linestyle='--')
    ax.vlines(x=b, ymin=0, ymax=fb, color='r', linestyle='--')
    ax.plot([a, b], [fa, fb], color='r', linestyle='--')

    ax.fill([a, a, m, b, b], [0, fa, fm, fb, 0], 'r', alpha=0.2)

    ax.set_title('Trapezoide')
    plt.grid(True)
    plt.legend()

    st.warning('Error: '+str(round(error,2))+'%')
    fig_placeholder.pyplot(fig)

def simpson3_8(var, func, a, b, start_range, end_range):
    global x
    x = sp.symbols(var)
    y = sp.sympify(func)

    m1 = (2 * a + b) / 3
    m2 = (a + 2 * b) / 3

    fa = y.subs({x: a}).evalf()
    fb = y.subs({x: b}).evalf()
    fm1 = y.subs({x: m1}).evalf()
    fm2 = y.subs({x: m2}).evalf()

    fig_placeholder = st.empty() # Espacio reservado para la figura

    # Regla de Simpson 3/8
    I = (b - a) / 8 * (fa + 3 * fm1 + 3 * fm2 + fb)

    I_real = sp.integrate(y, (x, a, b))
    error = np.abs((I_real - I) / I_real) * 100

    # Crear la figura
    fig, ax = plt.subplots()
    r = np.linspace(start_range, end_range, 100)
    fx = calculate_y(r, y)

    ax.set_title('${}$'.format(sp.latex(y)))
    ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
    ax.vlines(x=0, ymin=min(fx)-0.5, ymax=max(fx)+0.5, color='k')
    ax.hlines(y=0, xmin=min(r)-0.5, xmax=max(r)+0.5, color='k')
    ax.grid(True)

    # Límites xl y xu
    ax.vlines(x=0, ymin=min(fx), ymax=max(fx), color='k')
    ax.hlines(y=0, xmin=min(r), xmax=max(r), color='k')

    ax.vlines(x=a, ymin=0, ymax=fa, color='r', linestyle='--')
    ax.vlines(x=b, ymin=0, ymax=fb, color='r', linestyle='--')
    # ax.plot([a, b], [fa, fb], color='r', linestyle='--')

    ax.fill([a, a, m1, m2, b, b], [0, fa, fm1, fm2, fb, 0], 'r', alpha=0.2)

    ax.set_title(f'Regla Simpson {sp.latex(sp.S(3/8))}')
    plt.grid(True)
    plt.legend()

    st.warning('Error: '+str(round(error,2))+'%')
    fig_placeholder.pyplot(fig)

