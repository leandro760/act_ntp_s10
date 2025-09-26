import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)
print("Vista inicial:")
print(df.head())

def seleccion_empleados(df, id_individual=None, lista_ids=None, rango_ids=None):
    
    resultados = {}
    
    if id_individual is not None:
        try:
            resultados["Empleado individual"] = df.loc[id_individual]
        except KeyError:
            resultados["Empleado individual"] = f"Error: no existe el empleado con ID = {id_individual}"
    
    if lista_ids is not None:
        try:
            resultados["Lista empleados"] = df.loc[lista_ids]
        except KeyError as e:
            resultados["Lista empleados"] = f"Error: alguna ID en la lista no existe — {e}"
    
    if rango_ids is not None:
        inicio, fin = rango_ids
        try:
            resultados["Rango empleados"] = df.loc[inicio:fin]
        except KeyError as e:
            resultados["Rango empleados"] = f"Error: al usar rango ({inicio}, {fin}) — {e}"
        
    if not resultados:
        print("Empleado no existe.")
        return
    
    for clave, valor in resultados.items():
        print(f"\n--- {clave} ---")
        print(valor)
        print()  

seleccion_empleados(df, id_individual=3)
seleccion_empleados(df, lista_ids=[2, 4, 6])
seleccion_empleados(df, rango_ids=(15, 20))

