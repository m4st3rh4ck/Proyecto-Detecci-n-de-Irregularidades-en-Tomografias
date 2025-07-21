# Importamos la biblioteca NumPy, muy útil para trabajar con matrices y operaciones matemáticas.
import numpy as np

# Esta función calcula la **divergencia** de un campo vectorial 2D.
# u y v representan las componentes del movimiento (horizontal y vertical, respectivamente).
def calcular_divergencia(u, v):
    # Calculamos la derivada parcial de u con respecto a x (es decir, cómo cambia u en la dirección horizontal)
    du_dx = np.gradient(u, axis=1)  # axis=1 significa "columna", es decir, dirección horizontal
    
    # Calculamos la derivada parcial de v con respecto a y (es decir, cómo cambia v en la dirección vertical)
    dv_dy = np.gradient(v, axis=0)  # axis=0 significa "fila", es decir, dirección vertical
    
    # La divergencia es la suma de estas dos derivadas: mide si el campo "se expande" o "se contrae"
    return du_dx + dv_dy

# Esta función calcula el **rotacional** (en 2D) de un campo vectorial.
# Mide qué tanto "gira" o "rota" el flujo en cada punto del campo.
def calcular_rotacional(u, v):
    # Calculamos la derivada parcial de v con respecto a x
    dv_dx = np.gradient(v, axis=1)
    
    # Calculamos la derivada parcial de u con respecto a y
    du_dy = np.gradient(u, axis=0)
    
    # El rotacional en 2D se define como esta resta: qué tanto gira el campo alrededor de un punto
    return dv_dx - du_dy
