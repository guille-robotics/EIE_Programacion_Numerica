import numpy as np

def euler(f, t0, y0, t_end, h):
    """Método de Euler (RK1)"""
    t_vals = np.arange(t0, t_end + h, h)
    y_vals = np.zeros(len(t_vals))
    y_vals[0] = y0
    for i in range(1, len(t_vals)):
        y_vals[i] = y_vals[i-1] + h * f(t_vals[i-1], y_vals[i-1])
    return t_vals, y_vals

def heun(f, t0, y0, t_end, h):
    """Método de Heun (RK2)"""
    t_vals = np.arange(t0, t_end + h, h)
    y_vals = np.zeros(len(t_vals))
    y_vals[0] = y0
    for i in range(1, len(t_vals)):
        t_i = t_vals[i-1]
        y_i = y_vals[i-1]
        
        k1 = f(t_i, y_i)
        k2 = f(t_i + h, y_i + h * k1)
        
        y_vals[i] = y_i + (h / 2) * (k1 + k2)
    return t_vals, y_vals

def ralston(f, t0, y0, t_end, h):
    """Método de Ralston (RK2)"""
    t_vals = np.arange(t0, t_end + h, h)
    y_vals = np.zeros(len(t_vals))
    y_vals[0] = y0
    for i in range(1, len(t_vals)):
        t_i = t_vals[i-1]
        y_i = y_vals[i-1]
        
        k1 = f(t_i, y_i)
        k2 = f(t_i + (3/4)*h, y_i + (3/4)*h * k1)
        
        y_vals[i] = y_i + h * ( (1/3)*k1 + (2/3)*k2 )
    return t_vals, y_vals

def punto_medio(f, t0, y0, t_end, h):
    """Método del Punto Medio (RK2)"""
    t_vals = np.arange(t0, t_end + h, h)
    y_vals = np.zeros(len(t_vals))
    y_vals[0] = y0
    for i in range(1, len(t_vals)):
        t_i = t_vals[i-1]
        y_i = y_vals[i-1]
        
        k1 = f(t_i, y_i)
        k2 = f(t_i + 0.5*h, y_i + 0.5*h * k1)
        
        y_vals[i] = y_i + h * k2
    return t_vals, y_vals