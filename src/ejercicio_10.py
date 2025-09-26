# Implementa una función que realice un análisis completo usando .loc. La función debe:

# Crear múltiples vistas del DataFrame usando diferentes filtros
# Calcular métricas por departamento y ciudad
# Identificar empleados con características específicas (top performers, nuevos, etc.)
# Generar un reporte completo con todas las métricas

import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print(df.head())