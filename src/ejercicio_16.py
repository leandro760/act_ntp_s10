import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def seleccion_pasos_iloc(df):

    print("\nCada segunda fila:\n")
    print(df.iloc[::2].head().to_string())
    
    print("\nFilas en orden inverso:\n")
    print(df.iloc[::-1].head().to_string())
 
    print("\nCada quinta fila desde posición 2:\n")
    print(df.iloc[2::5].head().to_string())

    print("\nCada tercera fila, columnas pares:\n")
    cols_pares = list(range(0, len(df.columns), 2))
    print(df.iloc[::3, cols_pares].head().to_string())

seleccion_pasos_iloc(df)