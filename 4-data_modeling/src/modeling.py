from sklearn.linear_model import LinearRegression
from pandas import read_csv, get_dummies
from matplotlib.pyplot import scatter, show, xlabel, ylabel, plot
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from numpy import concatenate
from sklearn.neighbors import KNeighborsRegressor

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
#Prediccion de peso utilizando una variable (feature) a la vez
features = ["Height", "Age", "FAF", "CH2O"]

for feature in features:
    x = df[[feature]].values
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
    print(f"---{feature}---")
    print(f'Test R^2 for {feature} prediction for Weight: {r_score:.4f}') #Mas cercanos a 1, mejor
    print(f'MSE of the model: {mean_squared_error(y_test, y_pred)}') #Mas cercanos a 0, mejor

    # scatter(x_test, y_test, color = "black")
    # plot(x_test, y_pred, color="blue", linewidth=3)
    # show()

#Obtenemos los datos para el modelo
features = ['Height', 'Age']
x = df[features].values
y = df[["Weight"]].values

#Dividir los datos del dataset para entrenar y testing
x_train, x_test, y_train, y_test = train_test_split(x, y)

lr = LinearRegression()
#Entrenar el modelo (train)
lr.fit(x_train, y_train)
#Generamos la predicion pasado en los datos de prueba (test)
y_pred = lr.predict(x_test)

#Metricas del modelo
r_score = lr.score(x, y)
print(f"---{features}---")
print(f'Test R^2 for {features} prediction for Weight: {r_score:.4f}') #Mas cercanos a 1, mejor
print(f'MSE of the model: {mean_squared_error(y_test, y_pred)}') #Mas cercanos a 0, mejor

#Seleccionar features para el modelo con varios features
features_cat = ['family_history_with_overweight', 'FAVC', 'CAEC', 'CALC', 'MTRANS']
features = ["Height", "Age", "FAF", "CH2O"]
#Conviertiendo la variable categorica a algo que puede usar el modelo (encoding)
x_cat = get_dummies(df[features_cat]).values
#Obtenemos los valores de los numeros
x_num = df[features].values
#Combinando ambas columnas en un dataset de features
x = concatenate((x_num, x_cat), axis = 1)

y = df[["Weight"]].values

#Dividir los datos del dataset para entrenar y testing
x_train, x_test, y_train, y_test = train_test_split(x, y)

lr = LinearRegression()
#Entrenar el modelo (train)
lr.fit(x_train, y_train)
#Generamos la predicion pasado en los datos de prueba (test)
y_pred = lr.predict(x_test)

#Metricas del modelo
r_score = lr.score(x, y)
print(f"---ALL---")
print(f'Test R^2 for ALL prediction for Weight: {r_score:.4f}') #Mas cercanos a 1, mejor
print(f'MSE of the model: {mean_squared_error(y_test, y_pred)}') #Mas cercanos a 0, mejor

x = df[['Height', 'Age']].values
y = df['Weight'].values

#Dividir los datos del dataset para entrenar y testing
x_train, x_test, y_train, y_test = train_test_split(x, y)

knn = KNeighborsRegressor()
#Entrenar el modelo (train)
knn.fit(x_train, y_train)

#Metricas del modelo
print(f"---KNN---")
print(f'Score of the model: {knn.score(x_test, y_test)}')

