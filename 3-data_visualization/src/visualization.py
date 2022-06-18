from pandas import read_csv, to_datetime
from matplotlib.pyplot import scatter, show, title, ylabel, xlabel, plot, text

#Carga el archivo
df = read_csv("./data/books.csv", error_bad_lines=False)

#Generamos un grafico de calificaciones y reseñas
calificacion_promedio = df["average_rating"]
resennas_cantidad = df["text_reviews_count"]
title("Cantidad de reseñas comparado a la calificación promedio")
xlabel("Cantidad de reseñas")
ylabel("Calificación promedio")
scatter(resennas_cantidad, calificacion_promedio)
show()

# #Generamos un grafico de calificaciones y reseñas, marcando los puntos mas grandes de reseñas
# calificacion_promedio = df["average_rating"]
# resennas_cantidad = df["text_reviews_count"]
# title("Cantidad de reseñas comparado a la clasificación promedio")
# xlabel("Cantidad de reseñas")
# ylabel("Clasificación promedio")
# for index, libro in df.iterrows():
#     y = libro["average_rating"]
#     x = libro["text_reviews_count"]
#     plot(x,y, 'bo')
#     if libro["text_reviews_count"] > 40000:
#         text(x, y * (1 - 0.05), libro['title'], fontsize=12)
# scatter(resennas_cantidad, calificacion_promedio)
# show()

#Histogramas de ratings
df["average_rating"].plot(kind= 'hist', bins =30, figsize = (12, 12))
title("Histograma de calificaciones")
ylabel("Cantidad de calificaciones")
xlabel("Calificación promedio")
show()

#Lineas de libros por año
df["year"] = to_datetime(df["publication_date"].str.split("/").str[-1])
libros_anuales = df.groupby(["year"]).size().reset_index(name='counts')
annos = libros_anuales["year"]
cantidad_libros = libros_anuales["counts"]
print(libros_anuales)
title("Libros anuales")
ylabel("Cantidad de libros")
xlabel("Año")
plot(annos, cantidad_libros)
show()