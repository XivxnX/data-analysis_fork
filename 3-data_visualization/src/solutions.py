from pandas import read_csv
from matplotlib.pyplot import scatter, show, title, xlabel, ylabel, plot, legend, ylim, xlim, pie, Circle, gcf

# # Con los datos de las canciones de spotify, haga un gráfico de dispersión entre danceability (bailable) y energy (energía).
# spotify = read_csv("./data/spotify.csv")

# # bailable = spotify["danceability"]
# # energia = spotify["energy"]
# # xlabel("Bailable")
# # ylabel("Energía")
# # title("Bailable vs Energía en canciones")
# # scatter(bailable, energia)
# # show()

# # hip_hop = spotify.loc[spotify["genre"].isin(['hip hop'])]
# # bailable = hip_hop["danceability"]
# # energia = hip_hop["energy"]
# # xlabel("Bailable")
# # ylabel("Energía")
# # title("Bailable vs Energía en canciones de hip hop")
# # scatter(bailable, energia)
# # show()

# # # Con los datos de las canciones de spotify, genera un histograma de la duración de las canciones. Para hacer este gráfico más legible, pase el tiempo de milisegundos a segundos (puede redondear al más cercano).
# # spotify["duration_s"] = spotify["duration_ms"]/1000
# # spotify["duration_m"] = spotify["duration_s"]/60
# # spotify["duration_m"].plot(kind = 'hist')
# # title("Historgrama de la duración de las canciones")
# # ylabel("Cantidad de canciones")
# # xlabel("Duración de las canciones (minutos)")
# # show()

# # Con los datos de las canciones de spotify, genere un gráfico de líneas para los años de las canciones. Se quiere que se haga dos líneas dentro del gráfico, uno para la valencia (valence) promedio anual de las canciones y otra de la energía (energy). Haga una línea relacionada a los años. Puede encontrar documentación al respecto en el siguiente enlace: gráfico con múltiples líneas.
# spotify_anual = spotify.groupby(["year"]).mean().reset_index("year")
# print(spotify_anual)
# annos = spotify_anual["year"]
# ylabel("Caracteristica de la canción")
# xlabel("Años")
# energia = spotify_anual["energy"]
# valencia = spotify_anual["valence"]
# plot(annos, energia, label="Energia")
# plot(annos, valencia, label="Valencia")
# ylim(0, 1)
# legend()
# show()

# Con los datos de los libros, generar un gráfico de donas de los lenguajes de libros con matplotlib. Puede encontrar documentación al respecto en el siguiente enlace: gráfico de donas.
libros = read_csv("./data/books.csv", error_bad_lines = False)
lenguajes = libros["language_code"].value_counts().rename_axis("lenguaje").reset_index(name='cuenta')
pie(lenguajes["cuenta"], labels=lenguajes["lenguaje"])
circulo = Circle( (0,0), 0.7, color = 'white')
p = gcf()
p.gca().add_artist(circulo)
print(lenguajes)
show()