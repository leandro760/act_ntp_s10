import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def seleccion_basica_iloc(df):

    print("\nPrimera fila:\n")
    print(df.iloc[0].to_string())
  
    print("\nPrimeras 5 filas:\n")
    print(df.head().to_string())

    print("\nÚltima fila\n:")
    print(df.iloc[-1].to_string())

    print("\nFilas específicas (posiciones 0, 2, 4):\n")
    print(df.iloc[[0, 2, 4]].to_string())

seleccion_basica_iloc(df)