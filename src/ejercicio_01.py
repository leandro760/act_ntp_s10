import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def seleccion_basica_loc(df):

    print("\nEmpleado específico (ID 1):\n")
    empleado_especifico = df.loc[1]
    print(empleado_especifico.to_string())
    
    print("\nMúltiples empleados (IDs [1, 5, 10]):\n")
    multiples_empleados = df.loc[[1, 5, 10]]
    print(multiples_empleados.to_string())
    
    print("\nRango de empleados (IDs 1 a 5):\n")
    rango_empleados = df.loc[1:5]
    print(rango_empleados.to_string())

seleccion_basica_loc(df)