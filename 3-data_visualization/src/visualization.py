from pandas import read_csv
from matplotlib.pyplot import scatter, show, title, ylabel, xlabel, legend

#Carga el archivo
df = read_csv("./data/books.csv", error_bad_lines=False)

#Generamos un grafico de calificaciones y reseñas
calificacion_promedio = df["average_rating"]
resennas_cantidad = df["text_reviews_count"]
title("Cantidad de reseñas comparado a la clasificación promedio")
xlabel("Cantidad de reseñas")
ylabel("Clasificación promedio")
scatter(resennas_cantidad, calificacion_promedio)
show()