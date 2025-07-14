import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

df_case = pd.read_csv(r"Esercizi\Giorno 13\dataset_case.csv")

print(df_case.head())

X = df_case[["superficie", "stanze", "eta"]]
print(X.head())
Y = df_case["prezzo"]

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

model = LinearRegression()
model.fit(x_train, y_train)
print("Modello addestrato con successo!")

y_pred = model.predict(x_test)

print("Valutazione del modello:")
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R^2:", r2_score(y_test, y_pred))

features = X.columns
coefficients = model.coef_
intercept = model.intercept_

print(f"Intercetta: {intercept:.2f} €")
for feature, coef in zip(features, coefficients): print(f"Coefficiente per {feature}: {coef:.2f} € per unità")

print(" INTERPRETAZIONE DEI COEFFICIENTI:")
print(
    "Per ogni unità di superficie in più, il prezzo aumenta di circa {:.2f} €.".format(coefficients[0])
)
print(
    "Per ogni stanza in più, il prezzo aumenta di circa {:.2f} €.".format(coefficients[1])
)
print(
    "Per ogni anno in più di età della casa, il prezzo diminuisce di circa {:.2f} €.".format(coefficients[2])
)

plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred, alpha = 0.7, color = "blue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw = 2)
plt.xlabel("Prezzi Reali (€)")
plt.ylabel("Prezzi Predetti (€)")
plt.title("Prezzi Reali vs Prezzi Predetti")
plt.grid(True, alpha = 0.3)
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test - y_pred, alpha = 0.7, color = "green")
plt.axhline(0, color = "red", linestyle="--", lw = 2)
plt.xlabel("Prezzi Reali (€)")
plt.ylabel("Residui (€)")
plt.title("Residui dei Prezzi")
plt.grid(True, alpha = 0.3)
plt.tight_layout()
plt.show()

while True:
    user_input = input("Vuoi fare una previsione? (s/n): ").strip().lower()
    if user_input == "s":
        superficie = float(input("Inserisci la superficie in m²: "))
        stanze = int(input("Inserisci il numero di stanze: "))
        eta = int(input("Inserisci l'età della casa in anni: "))

        input_data = np.array([[superficie, stanze, eta]])
        predicted_price = model.predict(input_data)[0]

        print(f"Il prezzo previsto per la casa è di circa {predicted_price:.2f} €.")
    elif user_input == "n":
        print("Uscita dal programma.")
        break
    else:
        print("Input non valido. Rispondi con 's' per sì o 'n' per no.")