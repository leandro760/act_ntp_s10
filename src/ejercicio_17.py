import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def seleccion_avanzada_iloc(df):
  
    subconjunto = df.iloc[10:20, :5]
    print("\nSubconjunto filas 10-19, primeras 5 cols:\n")
    print(subconjunto.to_string())
    
    mask = df['salario'] > df['salario'].mean()
    seleccion_bool = df.iloc[mask.values]
    print(f"\nFilas donde salario > media ({len(seleccion_bool)}):\n")
    print(seleccion_bool.head().to_string())
 
    suma_salarios = df.iloc[:, df.columns.get_loc('salario')].sum()
    print(f"\nSuma de salarios:\n {suma_salarios:.2f}")
    
    num_cols = len(df.columns)
    cols_validas = [0, 2, min(5, num_cols - 1)]  
    vista_personal = df.iloc[::5, cols_validas]
    print("\nVista personalizada:\n")
    print(vista_personal.head().to_string())

seleccion_avanzada_iloc(df)