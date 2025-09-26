# Ejercicio 20: Análisis Completo con .iloc
# Implementa una función que realice un análisis completo usando .iloc. La función debe:

# Crear diferentes vistas del DataFrame usando posiciones
# Realizar análisis de muestras aleatorias vs sistemáticas
# Comparar rendimiento de diferentes métodos de selección
# Generar un reporte completo con métricas de las diferentes selecciones

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())