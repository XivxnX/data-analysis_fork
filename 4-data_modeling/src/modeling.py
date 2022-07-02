from sklearn.linear_model import LinearRegression
from pandas import read_csv
from matplotlib.pyplot import scatter, show, xlabel, ylabel

#Leemos los datos
df = read_csv('./data/obesity.csv')
print(df)

#Graficar relaciones con el peso
scatter(df["Height"], df["Weight"])
xlabel("Altura")
ylabel("Peso")
show()

scatter(df["Age"], df["Weight"])
xlabel("Edad")
ylabel("Peso")
show()

scatter(df["FAF"], df["Weight"])
xlabel("FAF")
ylabel("Peso")
show()

scatter(df["CH2O"], df["Weight"])
xlabel("CH2O")
ylabel("Peso")
show()