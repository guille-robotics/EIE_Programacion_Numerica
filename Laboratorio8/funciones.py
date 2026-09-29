import numpy as np

def rk4(f, t0, y0, t_end, h):
    """Método clásico de Runge-Kutta de cuarto orden (RK4)"""

    t_vals = np.arange(t0, t_end + h, h)
    y_vals = np.zeros(len(t_vals))
    y_vals[0] = y0
    
    for i in range(1, len(t_vals)):
        t_i = t_vals[i-1]
        y_i = y_vals[i-1]
        
        k1 = f(t_i, y_i)
        k2 = f(t_i + 0.5 * h, y_i + 0.5 * h * k1)
        k3 = f(t_i + 0.5 * h, y_i + 0.5 * h * k2)
        k4 = f(t_i + h, y_i + h * k3)
        
        y_vals[i] = y_i + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        
    return t_vals, y_vals

def error_relativo_porcentual(y_real, y_aprox):
    """Calcula el error relativo porcentual verdadero."""
    return np.abs((y_real - y_aprox) / y_real) * 100