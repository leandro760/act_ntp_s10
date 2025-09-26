# Ejercicio 8: Filtrado Avanzado con Funciones
# Crea una función que use funciones personalizadas con .loc. La función debe:

# Crear una función que clasifique salarios (bajo, medio, alto)
# Filtrar empleados con salario superior al promedio
# Filtrar empleados con salario en el percentil 75
# Mostrar distribución de cada categoría

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())