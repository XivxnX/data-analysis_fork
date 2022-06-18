from pandas import read_csv

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

