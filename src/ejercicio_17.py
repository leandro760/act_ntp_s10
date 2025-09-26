# Ejercicio 17: Selección Avanzada con .iloc
# Implementa una función que realice selecciones complejas. La función debe:

# Seleccionar subconjuntos específicos del DataFrame
# Usar arrays booleanos con .iloc
# Combinar .iloc con funciones de agregación
# Crear vistas personalizadas del DataFrame

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())