# Crear un objeto de tipo ndarray, con números enteros entre 64 hasta 1024.
import numpy as np

COLUMNAS_UNIDIMENSIONAL = 1024-64

# narray unidimensional
list = np.ndarray(shape=(COLUMNAS_UNIDIMENSIONAL),
                  dtype=float, buffer=None, order='F')
list.fill(0)

print(np.shape(list))

# Redimensionar a una matriz bidimensional que tenga las 1024 observaciones, pero que su dimensión tenga tanto el mismo número de filas como de columnas, con la finalidad de obtener una cuadrada.
# Crear una columna de datos aleatorios de 30 observaciones o registros, en la que se escojan dichos registros desde una lista de 10 nombres. Se debe repetir el proceso anterior para crear un set de números de cédulas aleatorio para cada uno de los nombres.
# Lista=[‘Andres’,’Maria’,’Manuel’,’Daniel’,’Sarah’,’Cristian’,’Violetta’,’Lucia’,’Jackson’,’Jose’]

# Concatenar un nuevo vector con las observaciones de los nombres y cédulas.
# Mostrar la posición del número más grande de las cédulas generadas del vector creado en el punto 4. Se debe investigar Slicing notation en numpy.
