import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def filtros_complejos(df):

    filtro_cambinado = df.loc[
        (df['activo'] == True) & 
        ((df['departamento'] == 'IT') | (df['departamento'] == 'Finanzas')) & 
        (df['salario'] > 60000) & 
        (df['edad'] < 45)
    ]
    print(f"\nEmpleados activos, de IT o Finanzas, con salario mayor a $60000 y edad menor a 45 años:\n {filtro_cambinado}")
    print("\nResumen estadístico:\n")
    print(filtro_cambinado[['edad', 'salario', 'experiencia_años']].describe())
    
    ciudades_espec = ['Bogotá', 'Medellín']
    filtro_ciudades = df.loc[
        (df['ciudad'].isin(ciudades_espec)) & 
        (df['experiencia_años'] > 10)
    ]
    print(f"\nEmpleados de Bogota y Medellin con experiencia mayor a 10 años:\n {filtro_ciudades}")
    print("\nResumen estadístico:\n")
    print(filtro_ciudades[['edad', 'salario', 'experiencia_años']].describe())


filtros_complejos(df)