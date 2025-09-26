import pandas as pd

df = pd.read_csv('data/dataset_general.csv')
df.set_index('empleado_id', inplace=True)

def filtros_simples(df):
   
    filtro_edad = df.loc[df['edad'] > 40]
    count_edad = len(filtro_edad)
    print(f"Empleados mayores de 40 años: {count_edad}")
    print(filtro_edad)
    print("\n" + "-"*40 + "\n")
    
  
    filtro_it = df.loc[df['departamento'] == 'IT']
    count_it = len(filtro_it)
    print(f"Empleados del departamento IT: {count_it}")
    print(filtro_it)
    print("\n" + "-"*40 + "\n")
    
    
    filtro_salario = df.loc[df['salario'] > 80000]
    count_salario = len(filtro_salario)
    print(f"Empleados con salario mayor a 80000: {count_salario}")
    print(filtro_salario)
    print("\n" + "-"*40 + "\n")


if __name__ == "__main__":

    filtros_simples(df)
