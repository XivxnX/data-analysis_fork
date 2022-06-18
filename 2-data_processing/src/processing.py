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

# Crear una file para los años
print("\n" * 5)
df["year"] = df["publication_date"].str.split("/").str[-1]
df["year"] = df["year"].astype(int)
print(df["year"])

# Obtener todos los lenguajes
print("\n" * 5)
lenguajes = df["language_code"].unique()
print(lenguajes)

#Seleccionar columnas que tengan ciertos valores
print("\n" * 5)
spanish_books = df.loc[df["language_code"] == "spa"]
print(spanish_books.head())
spanish_books.to_csv("./data/spanish_books.csv", index=False)

#Seleccionar columnas entre un rango de valores
print("\n" * 5)
df_200x = df.loc[(df["year"] >= 2000) & (df["year"] < 2010)]
print(df_200x.head())

#Contar cuantas veces aparece un valor por lenguaje
print(df["language_code"].value_counts())

#Seleccionar max de valores
print(df.groupby(['language_code'])["average_rating"].max())