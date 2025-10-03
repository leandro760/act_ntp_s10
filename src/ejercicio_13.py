import pandas as pd
import numpy as np

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def seleccion_multiples_filas_iloc(df):

    print("\nPosiciones específicas [0, 5, 10, 15]:\n")
    print(df.iloc[[0, 5, 10, 15]].to_string())
    
    np.random.seed(42) 
    filas_aleatorias = np.random.choice(df.index, size=5, replace=False)
    print("\nFilas aleatorias:\n")
    print(df.iloc[filas_aleatorias].to_string())
 
    combinado = pd.concat([df.iloc[[0, 99]], df.iloc[::20]])
    print("\nCombinado de filas (primera, última, cada 20):\n")
    print(combinado.to_string())
    
    seleccionadas = df.iloc[[0, 10, 20, 30, 40]]
    print("\nEstadísticas de selección:\n")
    print(seleccionadas[['edad', 'salario']].describe())

seleccion_multiples_filas_iloc(df)

