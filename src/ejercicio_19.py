import pandas as pd
import numpy as np

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def combinaciones_iloc(df):

    vista1 = df.iloc[:10, :]
    vista2 = df.iloc[-10:, :4]
    vista3 = df.iloc[::10, [0, 2, 5]]
    
    print("\nPrimeras 10 filas:\n")
    print(vista1.to_string())
    print("\nUltimas 10 y primeras 4 columnas:\n")
    print(vista2.to_string())
    print("\nCada 10, columnas 0,2,5):\n")
    print(vista3.to_string())
    
   
    np.random.seed(42)
    aleatoria = np.random.choice(len(df), 3, replace=False)
    sistematica = list(range(0, len(df), 20))
    combinada = np.unique(np.append(aleatoria, sistematica))
    print(f"\nCombinada aleatoria + sistemática\n ({len(combinada)}):")
    print(df.iloc[combinada].to_string())
   
    depts = df['departamento'].unique()
    muestras = []
    for dept in depts:
        idx_dept = df[df['departamento'] == dept].index
        pos_dept = np.where(df.index.isin(idx_dept))[0]
        if len(pos_dept) > 0:
            muestra_dept = np.random.choice(pos_dept, min(2, len(pos_dept)), replace=False)
            muestras.extend(muestra_dept)
    print(f"\nMuestras estratificadas por departamento:\n ({len(muestras)})")
    print(df.iloc[np.unique(muestras)].to_string())
    
    media_aleatoria = df.iloc[aleatoria]['salario'].mean()
    media_sistem = df.iloc[sistematica]['salario'].mean()
    print(f"\nComparación muestreo - Media aleatoria:\n {media_aleatoria:.2f}, Sistemática:\n {media_sistem:.2f}")

combinaciones_iloc(df)