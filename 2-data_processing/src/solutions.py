from pandas import read_csv

def guardar_primeras_cien_filas(df, columna, nombre_archivo_guardar):
    '''
    Obtiene las primeras 100 filas de una columna de un df

    df: El dataframe
    columna: Nombre de la columna que se quieren obtener los primeros 100 valores
    nombre_archivo_guardar: El nombre donde se va a guardar los primero 100 filas que se buscan de una columna

    '''
    df_ordenado = df.sort_values(by=columna, ascending=False)
    # print(df_ordenado["popularity"])
    top_100 = df_ordenado.head(100)

    top_100.to_csv(nombre_archivo_guardar, index=False)

# Lea el archivo de .\data\spotify.csv.
df = read_csv("./data/spotify.csv")

# Obtenga las cien canciones más populares (las más cercanas a 1).
print(df["popularity"])
guardar_primeras_cien_filas(df, "popularity", "./data/mas_populares.csv")
guardar_primeras_cien_filas(df, "valence", "./data/mas_felices.csv")

# Obtenga todos los géneros musicales únicos.
#Obtenemos todos los generos por fila
generos_por_fila = df["genre"].str.split(",").to_list()

#Pasarlo de una matriz a una lista de una dimension
generos = []
for fila in generos_por_fila:
    generos.extend(fila)
print(generos)

#Quitando los espacios adelante de las palabras en python
generos_stripped = []
for genero in generos:
    generos_stripped.append(genero.strip())
print(generos_stripped)

#Obtiene los generos unicos
generos_unicos = list(set(generos_stripped))
print(generos_unicos)

print(df["genre"].unique())

#Obtenga todas las canciones de la banda Coldplay.
coldplay_songs = df.loc[df['artist'].isin(["Coldplay"])]
coldplay_songs = coldplay_songs.drop_duplicates()
print(coldplay_songs)