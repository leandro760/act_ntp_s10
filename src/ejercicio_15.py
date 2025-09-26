# Ejercicio 15: Modificación de Datos con .iloc
# Crea una función que modifique datos usando .iloc. La función debe:

# Modificar valores en posiciones específicas
# Modificar un rango de celdas
# Modificar múltiples columnas a la vez
# Mostrar los cambios realizados

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())