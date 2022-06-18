from pandas import read_csv
from matplotlib.pyplot import scatter, show, title, ylabel, xlabel, plot, text

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

#Generamos un grafico de calificaciones y reseñas, marcando los puntos mas grandes de reseñas
calificacion_promedio = df["average_rating"]
resennas_cantidad = df["text_reviews_count"]
title("Cantidad de reseñas comparado a la clasificación promedio")
xlabel("Cantidad de reseñas")
ylabel("Clasificación promedio")
for index, libro in df.iterrows():
    y = libro["average_rating"]
    x = libro["text_reviews_count"]
    plot(x,y, 'bo')
    if libro["text_reviews_count"] > 40000:
        text(x, y * (1 - 0.05), libro['title'], fontsize=12)
scatter(resennas_cantidad, calificacion_promedio)
show()