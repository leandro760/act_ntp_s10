# Ejercicio 14: Selección de Columnas por Posición
# Implementa una función que seleccione columnas usando .iloc. La función debe:

# Seleccionar las primeras 3 columnas
# Seleccionar columnas específicas por posición
# Seleccionar la última columna
# Combinar selección de filas y columnas

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())