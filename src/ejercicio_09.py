# Ejercicio 9: Combinación de Filtros Complejos
# Desarrolla una función que combine múltiples tipos de filtros. La función debe:

# Filtrar empleados activos, de IT o Finanzas, con salario > 60000 y edad < 45
# Usar operadores lógicos complejos con paréntesis
# Filtrar empleados de ciudades específicas con experiencia > 10 años
# Crear un resumen estadístico de los grupos filtrados

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())