# Importamos funciones desde distintos módulos del proyecto "procesamiento"
# Estas funciones nos ayudarán a trabajar con imágenes y análisis vectorial

# Función para cargar imágenes y calcular el flujo óptico (movimiento entre dos imágenes)
from procesamiento.flujo_deformacion import cargar_imagen, calcular_flujo_optico

# Funciones para calcular la divergencia y el rotacional (propiedades matemáticas de campos vectoriales)
from procesamiento.analisis_vectorial import calcular_divergencia, calcular_rotacional

# Funciones para mostrar visualmente los resultados como mapas e imágenes
from procesamiento.visualizacion import mostrar_mapas, mostrar_campo_vectores

# Definimos las rutas (direcciones) de dos imágenes que se van a analizar
ruta_img1 = 'imagenes/imagen1.png'
ruta_img2 = 'imagenes/imagen2.png'

# Cargamos la primera imagen desde su ruta y la guardamos en la variable 'imagen1'
imagen1 = cargar_imagen(ruta_img1)

# Cargamos la segunda imagen desde su ruta y la guardamos en la variable 'imagen2'
imagen2 = cargar_imagen(ruta_img2)

# Calculamos el flujo óptico entre las dos imágenes.
# El flujo óptico nos dice cómo se han movido los objetos entre imagen1 e imagen2.
# 'u' y 'v' son componentes del movimiento horizontal y vertical respectivamente.
u, v = calcular_flujo_optico(imagen1, imagen2)

# Calculamos la **divergencia** del campo de movimiento.
# Esto indica si los objetos están "expandiéndose" (divergencia positiva) o "contrayéndose" (negativa).
div = calcular_divergencia(u, v)

# Calculamos el **rotacional** del campo de movimiento.
# Esto indica si los objetos están "girando" o hay algún tipo de rotación en el flujo.
rot = calcular_rotacional(u, v)

# Mostramos visualmente los mapas de divergencia y rotacional.
# También los guardamos como archivos de imagen porque se indicó `guardar=True`.
mostrar_mapas(div, rot, guardar=True)

# Finalmente, mostramos el campo de vectores (movimiento) sobre la imagen original.
# Así podemos ver hacia dónde y cuánto se movieron las cosas.
mostrar_campo_vectores(u, v, fondo=imagen1)
