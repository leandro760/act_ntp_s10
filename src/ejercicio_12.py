import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def seleccion_rangos_iloc(df):
   
    print("\nFilas del 10 al 20:\n")
    print(df.iloc[9:20].to_string())
 
    print("\nÚltimas 10 filas:\n")
    print(df.iloc[-10:].to_string())
    
    print("\nFilas pares:\n")
    print(df.loc[df.index % 2 == 0].head().to_string())
    
    print("\nCada tercera fila:\n")
    print(df.iloc[::3].head().to_string())

seleccion_rangos_iloc(df)