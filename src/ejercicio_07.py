import pandas as pd
from datetime import datetime

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def filtrado_fechas_loc(df):

    ingresaron_2022 = df.loc[df['fecha_ingreso'].dt.year == 2022]
    antig_2022 = (datetime.now() - ingresaron_2022['fecha_ingreso']).dt.days / 365.25
    print(f"\nEmpleados que ingresaron en 2022:\n {ingresaron_2022}")
    print(f"\nAntigüedad promedio: {antig_2022.mean():.2f} años")

    fecha_limite = datetime(2023, 1, 1)
    ultimos_2anos = df.loc[df['fecha_ingreso'] > fecha_limite]
    antig_ult2 = (datetime.now() - ultimos_2anos['fecha_ingreso']).dt.days / 365.25
    print(f"\nEmpleados que ingresaron en los últimos 2 años:\n {ultimos_2anos}")
    print(f"\nAntigüedad promedio: {antig_ult2.mean():.2f} años")

    primer_trim = df.loc[(df['fecha_ingreso'].dt.month >= 1) & (df['fecha_ingreso'].dt.month <= 3)]
    antig_primtrim = (datetime.now() - primer_trim['fecha_ingreso']).dt.days / 365.25
    print(f"\nEmpleados que ingresaron en el primer trimestre de cualquier año:\n {primer_trim}")
    print(f"\nAntigüedad promedio: {antig_primtrim.mean():.2f} años")

filtrado_fechas_loc(df)