# Ejercicio 11: Selección Básica con .iloc
# Implementa una función que use .iloc para seleccionar datos por posición. La función debe:

# Seleccionar la primera fila
# Seleccionar las primeras 5 filas
# Seleccionar la última fila
# Seleccionar filas específicas por posición

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())