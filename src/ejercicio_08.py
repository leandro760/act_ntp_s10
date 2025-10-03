import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def filtrado_funciones(df):

    def clasificar_salario(sal):
        if sal < 50000:
            return 'bajo'
        elif sal < 80000:
            return 'medio'
        else:
            return 'alto'
    
    df['clasificacion_salario'] = df['salario'].apply(clasificar_salario)
    print("\nDistribución de categorías de salario:")
    print(df['clasificacion_salario'].value_counts())
   
    salario_prom = df['salario'].mean()
    superiores_prom = df.loc[df['salario'] > salario_prom]
    print(f"\nSalario superior al promedio ({salario_prom:.2f}): {len(superiores_prom)} registros")
    print(superiores_prom['clasificacion_salario'].value_counts())
    
    p75 = df['salario'].quantile(0.75)
    percentil_75 = df.loc[df['salario'] >= p75]
    print(f"\nSalario en percentil 75 ({p75:.2f}): {len(percentil_75)} registros")
    print(percentil_75['clasificacion_salario'].value_counts())

filtrado_funciones(df)