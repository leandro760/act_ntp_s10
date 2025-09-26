# Ejercicio 6: Filtrado con Funciones de String
# Desarrolla una función que use métodos de string con .loc. La función debe:

# Filtrar empleados cuyo nombre contenga el dígito '1'
# Filtrar empleados cuyo apellido termine en '5'
# Filtrar empleados de ciudades que empiecen con 'B'
# Mostrar estadísticas de cada grupo encontrado

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())