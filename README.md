# Población por País - Pandas

Aplicación que lée datos desde una archivo CSV (world_population.csv) y el usuario puede buscar por país y le devolverá un grafico de barras (formato PNG) con los datos de población del mismo.
Los datos de poblacion serán por decada, desde los años 70s hasta los 2020s, y ademas la de este ultimo año (2022).

• Lo ejecutaremos por consola:

> Nos preguntará que país deseamos buscar:
![Dashboard](https://github.com/qarlosbaldovino/POBLACION_PORPAIS_PANDAS/blob/master/terminalone.png?raw=true)

No pasará nada en la terminal pero en los archivos aparecerá el archivo PNG del gráfico.
![Dashboard](https://github.com/qarlosbaldovino/POBLACION_PORPAIS_PANDAS/blob/master/Peru_bar.png?raw=true)

> Para ejecutar este programa deberá instalar WSL2 y Python en su terminal.
```bash
wsl --install
```

> Dentro del repositorio hay un archivo txt (requeriments.txt) donde estarán todas las dependencias necesarias, las instalaremos:
```bash
python3 -m pip install requeriments.txt
```

> Luego lo ejecutamos.
```bash
python3 population_country.py
```
