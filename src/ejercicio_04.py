import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def seleccion_columnas_especificas(df):

    nombre_salario = df.loc[:, ['nombre', 'salario']]
    print("\nNombre y salario de todos los empleados (primeras 10 filas):\n")
    print(nombre_salario.head(10).to_string())

    cols_rango = df.loc[:, 'nombre':'departamento']
    print("\nColumnas desde 'nombre' hasta 'departamento' (primeras 10 filas):\n")
    print(cols_rango.head(10).to_string())

    mayores_50 = df.loc[df['edad'] > 50, ['nombre', 'salario', 'edad']]
    print("\n3. Empleados mayores de 50 años: nombre, salario, edad (primeras 10 filas):\n")
    print(mayores_50.head(10).to_string())

seleccion_columnas_especificas(df)