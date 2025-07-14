import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

df_case = pd.read_csv(r"Esercizi\Giorno 13\CarPrice_Assignment.csv")
print(df_case.head())

# Regressione lineare multipla.
X = df_case[['enginesize', 'horsepower', 'curbweight']]
print(X.head())

Y = df_case["price"]
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

model = LinearRegression()
model.fit(x_train, y_train)
print("Modello addestrato con successo!")

y_pred = model.predict(x_test)

print("Valutazione del modello:")
print("R^2:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

features = X.columns
features = X.columns
coefficients = model.coef_
intercept = model.intercept_

print(f"Intercetta: {intercept:.2f} €")
for feature, coef in zip(features, coefficients): print(f"Coefficiente per {feature}: {coef:.2f}")

plt.scatter(y_test, y_pred, alpha = 0.7, color = "blue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw = 2)
plt.xlabel("Prezzi Reali (€)")
plt.ylabel("Prezzi Predetti (€)")
plt.title("Prezzi Reali vs Prezzi Predetti")
plt.grid(True, alpha = 0.3)
plt.show()

# Interpretazione dei coefficienti.
print(
    "Per ogni cc di cilindrata in meno, il prezzo aumenta di circa {:.2f} €.".format(coefficients[0]))
print(
    "Per ogni cavallo in meno, il prezzo aumenta di circa {:.2f} €.".format(coefficients[1]))
print(
    "Per ogni cavallo in meno, il prezzo aumenta di circa {:.2f} €.".format(coefficients[2]))

while True:
    user_input = input("Vuoi fare una previsione? (s/n): ").strip().lower()
    if user_input == "s":
        enginesize = float(input("Inserisci la cilindrata: "))
        horsepower = float(input("Inserisci i cavalli: "))
        curbweight = float(input("Inserisci il peso: "))
        prediction = model.predict([[enginesize, horsepower, curbweight]])
        print("Prezzo previsto: {:.2f} €".format(prediction[0]))
    elif user_input == "n":
        break
    else:
        print("Input non valido. Riprova.")