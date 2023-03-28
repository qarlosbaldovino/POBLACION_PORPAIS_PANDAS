import pandas as pd
import utils

## Leémos el CSV con un metodo de 
df = pd.read_csv('./world_population.csv')
country = input("Escribe el país que desea buscar: ")
result = df[df['Country/Territory'] == country.capitalize()]

if(len(result) > 0):
  valores = []
  labels, values = utils.get_population_pandas(result)
  utils.generate_bar_chart(country,labels,values)
  
else:
  print('País no encontrado.')
