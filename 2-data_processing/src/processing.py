from pandas import read_csv
from numpy import average, median, std

#Leer el archivo de Libros
df = read_csv("./data/books.csv", error_bad_lines=False)

print("\n" * 5)

#Viendo las columnas y las filas
print(df.columns)
print(df)
print(df.head(n=10))
print(df.tail())
print(df.info())

print("\n" * 5)

#Seleccionar una fila de datos
print(df["title"])

print("\n" * 5)

#Calcular estadisticas de la cantidad de calificaciones
average_rating_count = average(df["ratings_count"])
print(f"Calificaciones promedio: {average_rating_count:.2f}")

median_rating_count = median(df['ratings_count'])
print("Calificaciones mediana: " + str(median_rating_count)clock_settime)
# median(f"Calificaiones mediana: {median_rating_count}")