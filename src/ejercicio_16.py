# Ejercicio 16: Selección con Pasos
# Desarrolla una función que use pasos en la selección con .iloc. La función debe:

# Seleccionar cada segunda fila
# Seleccionar filas en orden inverso
# Seleccionar cada quinta fila empezando desde la tercera posición
# Combinar pasos en filas y columnas

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())