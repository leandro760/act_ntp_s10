# Ejercicio 5: Modificación de Datos con .loc
# Crea una función que modifique datos usando .loc. La función debe:

# Aumentar el salario en 10% a empleados de IT
# Cambiar el estado a inactivo para empleados mayores de 60 años
# Actualizar la ciudad a 'Bogotá' para empleados de RRHH
# Mostrar los cambios realizados antes y después

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())