import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def modificacion_datos_loc(df):
    df_mod = df.copy() 

    print("\nDATOS ORIGINALES:\n")
    print("Salarios de IT (primeras 10):\n")
    print(df_mod.loc[df_mod['departamento'] == 'IT', 'salario'].head(10).to_string())
    print("\nEstado de empleados mayores de 60 años (primeros 10):\n")
    print(df_mod.loc[df_mod['edad'] > 60, 'activo'].head(10).to_string())
    print("\nCiudad de RRHH (primeros 10):\n")
    print(df_mod.loc[df_mod['departamento'] == 'RRHH', 'ciudad'].head(10).to_string())
    
    df_mod['salario'] = df_mod['salario'].astype(float)
    df_mod.loc[df_mod['departamento'] == 'IT', 'salario'] *= 1.10
    
    df_mod.loc[df_mod['edad'] > 60, 'activo'] = False
    
    df_mod.loc[df_mod['departamento'] == 'RRHH', 'ciudad'] = 'Bogotá'

    print("\nDATOS MODIFICADOS:\n")
    print("Salarios de IT (primeras 10):\n")
    print(df_mod.loc[df_mod['departamento'] == 'IT', 'salario'].head(10).to_string())
    print("\nEstado de empleados mayores de 60 años (primeros 10):\n")
    print(df_mod.loc[df_mod['edad'] > 60, 'activo'].head(10).to_string())
    print("\nCiudad de RRHH (primeros 10):\n")
    print(df_mod.loc[df_mod['departamento'] == 'RRHH', 'ciudad'].head(10).to_string())

modificacion_datos_loc(df)