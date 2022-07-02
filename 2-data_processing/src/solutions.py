from pandas import read_csv

# Lea el archivo de .\data\spotify.csv.
df = read_csv("./data/spotify.csv")

# Obtenga las cien canciones más populares (las más cercanas a 1).
print(df["popularity"])

df_ordenado = df.sort_values(by="popularity", ascending=False)
print(df_ordenado["popularity"])
mas_populares = df_ordenado.head(100)

mas_populares.to_csv("./data/mas_populares.csv", index=False)