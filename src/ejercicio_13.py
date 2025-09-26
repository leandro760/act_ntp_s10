# Ejercicio 13: Selección de Múltiples Filas
# Desarrolla una función que seleccione múltiples filas no consecutivas. La función debe:

# Seleccionar filas usando una lista de posiciones específicas
# Seleccionar filas aleatorias
# Combinar diferentes métodos de selección
# Mostrar estadísticas de las filas seleccionadas

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())

