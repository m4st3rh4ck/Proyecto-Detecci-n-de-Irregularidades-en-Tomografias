import matplotlib.pyplot as plt
import numpy as np
import os

def mostrar_mapas(div, rot, guardar=True):
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    axs[0].imshow(div, cmap='seismic')
    axs[0].set_title("Mapa de Divergencia")
    axs[0].axis('off')

    axs[1].imshow(rot, cmap='twilight')
    axs[1].set_title("Mapa de Rotacional")
    axs[1].axis('off')

    plt.tight_layout()
    plt.show()

    if guardar:
        os.makedirs("resultados", exist_ok=True)
        plt.imsave("resultados/mapa_divergencia.png", div, cmap='seismic')
        plt.imsave("resultados/mapa_rotacional.png", rot, cmap='twilight')
        print("✅ Mapas guardados en la carpeta 'resultados/'")

def mostrar_campo_vectores(u, v, fondo=None, scale=1):
    h, w = u.shape
    Y, X = np.mgrid[0:h, 0:w]

    # En esta versión no filtramos por umbral: mostramos todos los vectores
    Xf = X
    Yf = Y
    uf = u
    vf = v

    plt.figure(figsize=(6, 6))

    # Mostramos imagen de fondo si se proporciona
    if fondo is not None:
        plt.imshow(fondo, cmap='gray')

    # Dibujamos todos los vectores (aunque sean pequeños) en color rojo
    plt.quiver(Xf, Yf, uf, vf, color='red',
               scale=scale, scale_units='xy', angles='xy', width=0.002)

    plt.title("Campo de Vectores (Flujo Óptico)")
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    print("✅ Campo de vectores mostrado con éxito")
