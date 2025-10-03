import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def filtrado_multiples_condiciones(df):
 
    it_alto_salario = df.loc[(df['departamento'] == 'IT') & (df['salario'] > 70000)]
    print(f"\nEmpleados de IT con salario > 70000:\n\n {it_alto_salario}")
    print("\nEstadísticas básicas:\n")
    print(it_alto_salario.describe())
    
    ventas_marketing = df.loc[(df['departamento'] == 'Ventas') | (df['departamento'] == 'Marketing')]
    print(f"\nEmpleados de Ventas o Marketing:\n\n {ventas_marketing}")
    print("\nEstadísticas básicas:\n")
    print(ventas_marketing.describe())
    
    activos_experiencia = df.loc[(df['activo'] == True) & (df['experiencia_años'] > 5)]
    print(f"\nEmpleados activos con mas de 5 años experiencia:\n\n {activos_experiencia}") 
    print("\nEstadísticas básicas:\n")
    print(activos_experiencia.describe())

filtrado_multiples_condiciones(df)
