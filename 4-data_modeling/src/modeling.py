from sklearn.linear_model import LinearRegression
from pandas import read_csv
from matplotlib.pyplot import scatter, show, xlabel, ylabel, plot
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#Leemos los datos
df = read_csv('./data/obesity.csv')
# print(df)

# #Graficar relaciones con el peso
# scatter(df["Height"], df["Weight"])
# xlabel("Altura")
# ylabel("Peso")
# show()

# scatter(df["Age"], df["Weight"])
# xlabel("Edad")
# ylabel("Peso")
# show()

# scatter(df["FAF"], df["Weight"])
# xlabel("Frecuencia de actividad física")
# ylabel("Peso")
# show()

# scatter(df["CH2O"], df["Weight"])
# xlabel("Cantidad de agua digerida diaria")
# ylabel("Peso")
# show()

x = df[["Height"]].values
y = df[["Weight"]].values # Target variable

#Dividir los datos del dataset para entrenar y testing
x_train, x_test, y_train, y_test = train_test_split(x, y)

lr = LinearRegression()
#Entrenar el modelo (train)
lr.fit(x_train, y_train)
#Generamos la predicion pasado en los datos de prueba (test)
y_pred = lr.predict(x_test)

#Metricas del modelo
r_score = lr.score(x, y)
print(f'Test R^2 for {"Height"} prediction for Weight: {r_score:.4f}') #Mas cercanos a 1, mejor
print(f'MSE of the model: {mean_squared_error(y_test, y_pred)}') #Mas cercanos a 0, mejor

scatter(x_test, y_test, color = "black")
plot(x_test, y_pred, color="blue", linewidth=3)
show()