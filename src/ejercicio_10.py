import pandas as pd
from datetime import datetime

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def analisis_completo_loc(df):

    vista_activos_it = df.loc[(df['activo'] == True) & (df['departamento'] == 'IT')]
    vista_nuevos = df.loc[df['fecha_ingreso'] > datetime(2023, 1, 1)]
    vista_top_salario = df.loc[df['salario'] > df['salario'].quantile(0.9)]
    
    metricas_dept = df.loc[:, ['departamento', 'salario', 'edad']].groupby('departamento').agg(['mean', 'count'])
    metricas_ciudad = df.loc[:, ['ciudad', 'experiencia_años', 'activo']].groupby('ciudad').agg(['mean', 'sum'])
    
    top_performers = df.loc[(df['salario'] > 90000) & (df['experiencia_años'] > 10)]
    nuevos_activos = df.loc[(df['activo'] == True) & (df['fecha_ingreso'] > datetime(2024, 1, 1))]

    print("\nVISTAS:\n")
    print(f"Activos IT: {len(vista_activos_it)}")
    print(f"Nuevos: {len(vista_nuevos)}")
    print(f"Top Salario: {len(vista_top_salario)}")
    
    print("\nMetricas por departamento:\n")
    print(metricas_dept)
    
    print("\nMetricas Por Ciudas:\n")
    print(metricas_ciudad)
    
    print(f"\nTop Performes:\n {len(top_performers)}")
    print(top_performers[['nombre', 'salario', 'experiencia_años']].head())
    
    print(f"\nNuevos Activos:\n {len(nuevos_activos)}")
    print(nuevos_activos[['nombre', 'fecha_ingreso']].head())

analisis_completo_loc(df)