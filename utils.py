import matplotlib.pyplot as plt

def get_population_pandas(data):
  population = {
    '2022' : data['2022 Population'].values[0],
    '2020' : data['2020 Population'].values[0],
    '2015' : data['2015 Population'].values[0],
    '2010' : data['2010 Population'].values[0],
    '2000' : data['2000 Population'].values[0],
    '1990' : data['1990 Population'].values[0],
    '1980' : data['1980 Population'].values[0],
    '1970' : data['1970 Population'].values[0],
  }
  return list(population.keys()), list(population.values())

def get_population(country_dict):
  population_dict = {
    '2022' : int(country_dict['2022 Population']),
    '2020' : int(country_dict['2020 Population']),
    '2015' : int(country_dict['2015 Population']),
    '2010' : int(country_dict['2010 Population']),
    '2000' : int(country_dict['2000 Population']),
    '1990' : int(country_dict['1990 Population']),
    '1980' : int(country_dict['1980 Population']),
    '1970' : int(country_dict['1970 Population']),
  }
  # retornamos keys: labels y values: valores de poblacion
  return population_dict.keys(), population_dict.values()

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

def generate_bar_chart(country,x,y):
  figure, coordenadas = plt.subplots()
  coordenadas.bar(x,y)
  plt.savefig(f'./{country}_bar.png')

def generate_pie_chart(country,x,y):
  figure, coordenadas = plt.subplots()
  coordenadas.pie(y,labels=x)
  coordenadas.axis('equal')
  plt.savefig(f'./images/8. {country}_pie.png')