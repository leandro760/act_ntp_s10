# Ejercicio 7: Filtrado por Fechas
# Implementa una función que filtre por fechas usando .loc. La función debe:

# Filtrar empleados que ingresaron en 2022
# Filtrar empleados que ingresaron en los últimos 2 años
# Filtrar empleados que ingresaron en el primer trimestre de cualquier año
# Calcular la antigüedad promedio de cada grupo

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())