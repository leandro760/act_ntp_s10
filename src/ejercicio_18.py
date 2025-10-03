import pandas as pd
import numpy as np

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def listas_indices_dinamicas(df):

    indices_altos_sal = df.index[df['salario'] > 80000].tolist()
    print(f"\nÍndices altos salario:\n {len(indices_altos_sal)}")
    
    posiciones_jovenes = np.where(df['edad'] < 30)[0]
    print(f"\nPosiciones empleados menores de 30 años:\n {len(posiciones_jovenes)}")

    p90_pos = np.where(df['salario'] >= df['salario'].quantile(0.9))[0]
    seleccion_p90 = df.iloc[p90_pos]
    print(f"\nSelección porcentaje 90 salario:\n ({len(seleccion_p90)}):")
    print(seleccion_p90.head().to_string())

    muestra_aleatoria = df.sample(n=5).index.tolist()
    print("\nMuestra aleatoria (5):\n")
    print(df.loc[muestra_aleatoria].to_string())  

listas_indices_dinamicas(df)