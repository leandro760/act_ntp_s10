# Ejercicio 19: Combinaciones de .iloc
# Desarrolla una función que combine diferentes usos de .iloc. La función debe:

# Crear múltiples vistas usando diferentes patrones de selección
# Combinar selección aleatoria con selección sistemática
# Usar .iloc para crear muestras estratificadas
# Comparar diferentes métodos de muestreo

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())