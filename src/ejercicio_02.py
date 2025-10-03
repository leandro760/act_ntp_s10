import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def filtrado_condiciones_simples(df):

    mayores_40 = df.loc[df['edad'] > 40]
    print(f"\nEmpleados mayores de 40 años: {len(mayores_40)} registros\n")
    print(mayores_40.head().to_string())
    
    dept_it = df.loc[df['departamento'] == 'IT']
    print(f"\nEmpleados del departamento 'IT': {len(dept_it)} registros\n")
    print(dept_it.head().to_string())
    
    salario_alto = df.loc[df['salario'] > 80000]
    print(f"\nEmpleados con salario mayor a 80000: {len(salario_alto)} registros\n")
    print(salario_alto.head().to_string())

filtrado_condiciones_simples(df)