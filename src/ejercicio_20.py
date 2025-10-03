import pandas as pd
import numpy as np
import time

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def analisis_completo_iloc(df):
   
    vista_completa = df.iloc[:, :]
    vista_parcial = df.iloc[::2, :5] 
    vista_final = df.iloc[-20:, -3:]  
    
    print(f"\nVista parcial:\n {len(vista_parcial)} filas")
    print(vista_parcial.head().to_string())
    print(f"\nVista final:\n {len(vista_final)} filas")
    print(vista_final.head().to_string())
 
    np.random.seed(42)
    tam_muestra = 10
    indices_aleatorios = np.random.choice(len(df), tam_muestra, replace=False)
    indices_sistematicos = np.arange(0, len(df), len(df)//tam_muestra)
    
    muestra_aleatoria = df.iloc[indices_aleatorios]
    muestra_sistematica = df.iloc[indices_sistematicos]
    
    media_sal_aleat = muestra_aleatoria['salario'].mean()
    media_sal_sist = muestra_sistematica['salario'].mean()
    media_sal_total = df['salario'].mean()
    
    print(f"\nMedia salario total: {media_sal_total:.2f}\n")
    print(f"\nMedia aleatoria: {media_sal_aleat:.2f}\n") 
    print(f"\nMedia sistemática: {media_sal_sist:.2f}\n")
    
    start = time.time()
    _ = df.iloc[:50, :]
    tiempo_rango = time.time() - start
    
    start = time.time()
    _ = df.iloc[np.random.choice(len(df), 50, replace=False)]
    tiempo_aleatorio = time.time() - start
    
    print(f"Tiempo selección rango: {tiempo_rango:.6f}\n")
    print(f"Tiempo selección aleatoria: {tiempo_aleatorio:.6f}\n")

    reporte = {
        'Método': ['Total', 'Aleatoria', 'Sistemática'],
        'N Filas': [len(df), tam_muestra, len(muestra_sistematica)],
        'Media Salario': [media_sal_total, media_sal_aleat, media_sal_sist],
        'Desv Salario': [df['salario'].std(), muestra_aleatoria['salario'].std(), muestra_sistematica['salario'].std()]
    }
    reporte_df = pd.DataFrame(reporte)
    print("\nReporte Completo\n")
    print(reporte_df.to_string(index=False))

analisis_completo_iloc(df)