# Ejercicio 4: Selección de Columnas Específicas
# Implementa una función que seleccione columnas específicas con .loc. La función debe:

# Seleccionar solo nombre y salario de todos los empleados
# Seleccionar un rango de columnas desde nombre hasta departamento
# Combinar filtro de filas y columnas para empleados mayores de 50 años
# Mostrar las primeras 10 filas de cada selección

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())