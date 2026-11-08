# Implementación de Arreglos Multidimensionales en Ingeniería

Este repositorio contiene la resolución de cinco problemas prácticos de ingeniería aplicando arreglos multidimensionales (2D, 3D y N-D). Las soluciones están desarrolladas en Python, aprovechando las capacidades del cómputo científico.

## Requisitos previos

Para ejecutar el código, necesitas instalar las siguientes dependencias:

pip install numpy matplotlib scipy


## Descripción de las Soluciones y Enfoque

### Problema 1: Análisis de Fuerzas (Estática)
* **Enfoque:** Se utilizó una matriz 2D (3x3) para representar el sistema de fuerzas. Aplicando la tercera ley de Newton (acción y reacción) y las leyes de la estática en equilibrio, las reacciones de los apoyos se calculan como el negativo exacto de las fuerzas externas aplicadas.
* **Eficiencia:** En lugar de iterar con bucles `for` celda por celda, se aplicó la vectorización matemática directa de matrices (`reacciones = -fuerzas`), reduciendo drásticamente la complejidad computacional y el tiempo de ejecución.

### Problema 2: Simulación de Fluido en 3D
* **Enfoque:** Se modeló el estado del fluido en un tensor 4D de dimensiones `(3, 3, 3, 3)`, donde las tres primeras dimensiones son el espacio tridimensional y la última almacena las magnitudes físicas del fluido (presión, temperatura, velocidad).
* **Eficiencia:** Para la simulación de propagación de ondas (actualización del estado basada en celdas vecinas), se evitó una triple iteración anidada. En su lugar, se utilizó una convolución espacial matemática mediante la función `uniform_filter` de SciPy, la cual ejecuta el cálculo subyacente en lenguaje C, siendo órdenes de magnitud más rápida que la iteración en Python nativo.

### Problema 3: Procesamiento de Imágenes Médicas 3D
* **Enfoque:** El conjunto de capas 2D (por ejemplo, cortes de Resonancia Magnética o TAC) se modela de forma natural como un volumen 3D. El ruido se mitigó aplicando un filtro espacial tridimensional (filtro de promedios o suavizado).
* **Eficiencia:** Al tratar todas las capas como un solo bloque de memoria contigua (gracias a la estructura subyacente de NumPy), el suavizado se aplica de forma matricial en una sola pasada a todo el volumen, logrando una complejidad de tiempo eficiente y minimizando el uso de caché del procesador.

### Problema 4: Manejo de Sensores (Serie de Tiempo Multivariante)
* **Enfoque:** Se utilizó una matriz bidimensional de 5x5, donde las filas representan el eje temporal (momentos en el tiempo) y las columnas representan unidades físicas independientes (sensores).
* **Eficiencia:** El uso de las funciones de agregación por ejes preconstruidas (`np.mean(axis=0)` y `np.std(axis=0)`) permite condensar las métricas de las columnas de manera completamente vectorial. Se calcularon promedios y desviaciones estándar simultáneamente para todos los sensores sin requerir un recorrido secuencial.

### Problema 5: Álgebra Lineal en Sistemas Cartesianos
* **Enfoque:** Los vértices espaciales se organizaron en una matriz bidimensional de tamaño (N x 2). Se definió una matriz de transformación estándar que combina una rotación (ej. 45°) y un escalado espacial mediante funciones trigonométricas.
* **Eficiencia:** El mapeo de coordenadas se ejecutó empleando el producto punto de matrices (`A @ B.T`). Este cálculo utiliza las rutinas altamente optimizadas de álgebra lineal (BLAS - Basic Linear Algebra Subprograms), lo que permite transformar miles o millones de coordenadas simultáneamente en una sola instrucción vectorial a nivel de CPU.