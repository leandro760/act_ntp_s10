# Ejercicio 12: Selección con Rangos
# Crea una función que use rangos con .iloc. La función debe:

# Seleccionar filas del 10 al 20
# Seleccionar las últimas 10 filas
# Seleccionar filas pares
# Seleccionar cada tercera fila

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())