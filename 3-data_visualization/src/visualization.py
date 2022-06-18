from pandas import read_csv
from matplotlib.pyplot import scatter, show

#Carga el archivo
df = read_csv("./data/books.csv", error_bad_lines=False)

calificacion_promedio = df["average_rating"]
resennas_cantidad = df["text_reviews_count"]
scatter(calificacion_promedio, resennas_cantidad)
show()