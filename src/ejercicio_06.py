import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df.set_index('empleado_id', inplace=True)

def filtrado_string_loc(df):
  
    nombres_con_1 = df.loc[df['nombre'].str.contains('1')]
    print(f"\nNombres con '1':\n {nombres_con_1}\n")
    print("\nEstadísticas:\n")
    print(nombres_con_1['edad'].describe())
   
    apellidos_fin_5 = df.loc[df['apellido'].str.endswith('5')]
    print(f"\nApellidos terminan en '5':\n {apellidos_fin_5}\n")
    print("\nEstadísticas:\n")
    print(apellidos_fin_5['salario'].describe())
    
    ciudades_b = df.loc[df['ciudad'].str.startswith('B')]
    print(f"\nCiudades empiezan con 'B':\n {ciudades_b}\n")
    print("\nEstadísticas:\n")
    print(ciudades_b['experiencia_años'].describe())

filtrado_string_loc(df)