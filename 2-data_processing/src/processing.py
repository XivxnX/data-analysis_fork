from pandas import DataFrame, read_csv
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
print("Calificaciones mediana: " + str(median_rating_count))
# median(f"Calificaiones mediana: {median_rating_count}")

std_rating_count = std(df["ratings_count"])
print(f"Calificaciones std: {std_rating_count:.2f}")

print("\n" * 5)

#Guardar datos de estadisticas en un archivos
data = [["Average", average_rating_count], ["Median", median_rating_count], ["Std", std_rating_count]]
df_statistics = DataFrame(data, columns=["statistic", "value"])
df_statistics.to_csv("./data/statistics_books_rating_count.csv", index=False)

#Crear una nueva fila en el df
df["ratings_vs_review_count"] = df["ratings_count"] / df["text_reviews_count"]
print(df)

print("\n" * 5)
df["year"] = df["publication_date"].str.split("/").str[-1]
df["year"] = df["year"].astype(int)
print(df["year"])

