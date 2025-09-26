# Ejercicio 18: Trabajo con Listas de Índices
# Crea una función que trabaje con listas de índices dinámicas. La función debe:

# Generar listas de índices basadas en condiciones
# Encontrar posiciones que cumplan criterios específicos
# Seleccionar filas basadas en percentiles
# Mostrar diferentes muestras del DataFrame


import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())