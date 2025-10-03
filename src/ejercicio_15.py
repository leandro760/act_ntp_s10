import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def modificacion_datos_iloc(df):
    df_mod = df.copy()

    col_salario = df_mod.columns.get_loc('salario')
    col_edad = df_mod.columns.get_loc('edad')
    col_activo = df_mod.columns.get_loc('activo')

    print("\nORIGINAL:\n")
    print("\nValor:\n", df_mod.iloc[0,1])
    print("\nRango:\n", df_mod.iloc[0:3, col_salario].to_string())
    
    df_mod.iloc[0, 1] = 'Nombre Modificado'
    
    df_mod.iloc[0:3, col_salario] = 100000  
    
    df_mod.iloc[5:10, [col_edad, col_activo]] = [30, True]  #
 
    print("\nMODIFICADO:\n")
    print("\nValor:\n", df_mod.iloc[0,1])
    print("\nRango:\n", df_mod.iloc[0:3, col_salario].to_string())
    print("\nRango:\n", df_mod.iloc[5:10, col_edad].to_string())
    print("\nRango:\n", df_mod.iloc[5:10, col_activo].to_string())

modificacion_datos_iloc(df)