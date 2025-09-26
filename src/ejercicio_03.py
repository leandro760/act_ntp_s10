# Ejercicio 3: Filtrado con Múltiples Condiciones
# Desarrolla una función que combine múltiples condiciones con .loc. La función debe:

# Filtrar empleados de IT con salario mayor a 70000
# Filtrar empleados de Ventas o Marketing
# Filtrar empleados activos con más de 5 años de experiencia
# Mostrar estadísticas básicas de cada grupo filtrado
import pandas as pd

# Supón que ya cargaste tu DataFrame:
df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print("Primeras filas del df:")
print(df.head())

