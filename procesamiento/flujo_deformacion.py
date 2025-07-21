# Importamos OpenCV (cv2) para trabajar con imágenes y video
# También importamos NumPy (np) para manejar operaciones matemáticas con matrices
import cv2
import numpy as np

# Esta función se encarga de cargar una imagen desde el disco, convertirla a escala de grises,
# redimensionarla a un tamaño específico y normalizar sus valores de 0 a 1
def cargar_imagen(path, tamaño=(256, 256)):
    # Leemos la imagen desde la ruta especificada en 'path'
    # La opción cv2.IMREAD_GRAYSCALE hace que la imagen se cargue en blanco y negro (1 canal)
    imagen = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Si no se pudo cargar la imagen (por ejemplo, si la ruta no existe), mostramos un error
    if imagen is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen en: {path}")

    # Redimensionamos la imagen al tamaño deseado (por defecto 256x256 píxeles)
    imagen = cv2.resize(imagen, tamaño)

    # Convertimos los valores de los píxeles a tipo float32 y los normalizamos dividiendo entre 255
    # Esto transforma los valores de 0–255 a un rango de 0.0–1.0
    imagen = imagen.astype(np.float32) / 255.0

    # Devolvemos la imagen ya lista para ser utilizada en otros procesos
    return imagen

# Esta función calcula el flujo óptico entre dos imágenes en escala de grises
# El flujo óptico representa cómo se han movido los objetos (píxeles) de la primera imagen a la segunda
def calcular_flujo_optico(im1, im2):
    # Usamos el algoritmo de Farneback para calcular el flujo óptico denso
    flujo = cv2.calcOpticalFlowFarneback(
        im1,         # Imagen anterior (fotograma 1)
        im2,         # Imagen actual (fotograma 2)
        None,        # No usamos un flujo inicial
        pyr_scale=0.5,   # Escala para construir pirámides de imágenes (para detectar movimientos grandes)
        levels=3,        # Número de niveles de la pirámide (resoluciones distintas)
        winsize=15,      # Tamaño de la ventana que se usa para comparar movimiento
        iterations=3,    # Número de iteraciones por nivel
        poly_n=5,        # Tamaño del vecindario para encontrar patrones
        poly_sigma=1.2,  # Desviación estándar para el filtro de suavizado
        flags=0          # Sin opciones especiales adicionales
    )

    # Extraemos las componentes horizontales (u) y verticales (v) del flujo óptico
    u = flujo[..., 0]  # Movimiento en el eje x (horizontal)
    v = flujo[..., 1]  # Movimiento en el eje y (vertical)

    # Devolvemos ambas matrices: una para el movimiento horizontal y otra para el vertical
    return u, v
