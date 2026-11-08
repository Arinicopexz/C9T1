import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter

def problema_1_fuerzas():
    print("Problema 1: Análisis de Fuerzas")
    # Matriz 3x3 que representa las fuerzas externas aplicadas en los nodos (en Newtons)
    fuerzas_externas = np.array([
        [10.0, -5.0, 0.0],
        [0.0,  20.0, -10.0],
        [-15.0, 0.0, 25.0]
    ])
    
    # Por la primera ley (estática), la suma de fuerzas debe ser cero.
    # Reacciones = -Fuerzas_Externas
    reacciones = -fuerzas_externas
    
    print("Fuerzas Externas:\n", fuerzas_externas)
    print("Reacciones calculadas en los nodos:\n", reacciones)
    


def problema_2_fluido():
    print("Problema 2: Simulación de Fluido en 3D")
    # Dimensiones: 3x3x3. Propiedades: Presión, Temperatura, Velocidad_P
    # Forma del arreglo: (3, 3, 3, 3)
    fluido = np.random.rand(3, 3, 3, 3) * 100 
    
    # Extraemos la capa de presión para la simulación de propagación
    presion = fluido[:, :, :, 0]
    
    print("Presión inicial (Capa z=0):\n", presion[:, :, 0])
    
    # Simulación del paso del tiempo 
    # Cada celda se actualiza al promedio de sus celdas vecinas
    presion_actualizada = uniform_filter(presion, size=3, mode='constant')
    
    # Actualizamos el estado del fluido
    fluido[:, :, :, 0] = presion_actualizada
    
    print("Presión tras un paso de propagación (Capa z=0):\n", fluido[:, :, :, 0])
    print("\n")


def problema_3_imagenes_medicas():
    print("Problema 3: Análisis de Imágenes Médicas 3D")
    # Simulamos un volumen 3D de imágenes médicas (ej. Resonancia Magnética de 10x10x10)
    # con ruido aleatorio
    volumen_original = np.random.normal(loc=50, scale=10, size=(10, 10, 10))
    ruido = np.random.normal(loc=0, scale=20, size=(10, 10, 10))
    volumen_ruidoso = volumen_original + ruido
    
    # Filtro de promedio (suavizado) para reducir el ruido en 3D
    volumen_suavizado = uniform_filter(volumen_ruidoso, size=3)
    
    # Visualizamos una sola capa (profundidad z=5) para comparar
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    ax1.imshow(volumen_ruidoso[:, :, 5], cmap='gray')
    ax1.set_title("Capa 5 - Con Ruido")
    ax2.imshow(volumen_suavizado[:, :, 5], cmap='gray')
    ax2.set_title("Capa 5 - Suavizada (Filtro Promedio)")
    plt.suptitle("Problema 3: Suavizado de Imagen Médica 3D")
    plt.show()
    print("Filtro de suavizado aplicado y visualizado.\n")


def problema_4_sensores():
    print("Problema 4: Manejo de Datos de Sensores")
    # Matriz 5x5: 5 filas (momentos de tiempo) x 5 columnas (sensores)
    # Temperaturas simuladas entre 20 y 30 grados
    datos_sensores = np.random.uniform(20.0, 30.0, size=(5, 5))
    
    # Eje 0 (columnas) = métricas por sensor a lo largo del tiempo
    promedios_sensores = np.mean(datos_sensores, axis=0)
    desviacion_sensores = np.std(datos_sensores, axis=0)
    
    # Eje 1 (filas) = métricas globales en cada momento de tiempo
    promedios_tiempo = np.mean(datos_sensores, axis=1)
    
    print("Datos de sensores (5x5):\n", np.round(datos_sensores, 2))
    print("Promedio por sensor:\n", np.round(promedios_sensores, 2))
    print("Desviación estándar por sensor:\n", np.round(desviacion_sensores, 2))
    
    # Visualización
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Mapa de calor de las lecturas
    cax = ax1.matshow(datos_sensores, cmap='hot')
    fig.colorbar(cax, ax=ax1)
    ax1.set_title("Lecturas de Temperatura (Sensores vs Tiempo)")
    ax1.set_xlabel("Sensores")
    ax1.set_ylabel("Momento en el tiempo")
    
    # Gráfico de barras de promedios por sensor
    sensores = ['S1', 'S2', 'S3', 'S4', 'S5']
    ax2.bar(sensores, promedios_sensores, yerr=desviacion_sensores, capsize=5, color='orange')
    ax2.set_title("Temperatura Promedio por Sensor")
    ax2.set_ylabel("Grados C°")
    plt.show()
    print("Análisis de sensores visualizado.\n")


def problema_5_transformacion():
    print("Problema 5: Transformación de Coordenadas")
    # Conjunto de puntos en 2D formando un cuadrado (Matriz Nx2)
    puntos_originales = np.array([
        [0, 0],
        [1, 0],
        [1, 1],
        [0, 1],
        [0, 0] # Cerrar el cuadrado
    ])
    
    # Matriz de Transformación Lineal (Rotación de 45 grados y escalado de 2x)
    theta = np.radians(45)
    escala = 2
    matriz_transformacion = np.array([
        [np.cos(theta)*escala, -np.sin(theta)*escala],
        [np.sin(theta)*escala,  np.cos(theta)*escala]
    ])
    
    # Aplicar transformación: Multiplicación de matrices (Puntos * Matriz^T)
    puntos_transformados = puntos_originales @ matriz_transformacion.T
    
    # Visualización
    plt.figure(figsize=(6, 6))
    plt.plot(puntos_originales[:, 0], puntos_originales[:, 1], marker='o', label='Original')
    plt.plot(puntos_transformados[:, 0], puntos_transformados[:, 1], marker='x', label='Transformado (Rotado + Escalado)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.title("Problema 5: Transformación Lineal de Coordenadas")
    plt.axis('equal')
    plt.show()
    print("Transformación aplicada y visualizada.\n")


if __name__ == '__main__':
    problema_1_fuerzas()
    problema_2_fluido()
    problema_3_imagenes_medicas()
    problema_4_sensores()
    problema_5_transformacion()