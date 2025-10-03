import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def seleccion_columnas_iloc(df):

    print("\nPrimeras 3 columnas (todas las filas, primeras 5):\n")
    print(df.iloc[:5, :3].to_string())

    print("\nColumnas específicas (posiciones 1, 3, 5):\n")
    print(df.iloc[:5, [1, 3, 5]].to_string())
   
    print("\nÚltima columna (primeras 5 filas):\n")
    print(df.iloc[:5, -1].to_string())

    print("\nPrimeras 5 filas y columnas 0, 1, 2, 4:\n")
    print(df.iloc[:5, [0, 1, 2, 4]].to_string())

seleccion_columnas_iloc(df)