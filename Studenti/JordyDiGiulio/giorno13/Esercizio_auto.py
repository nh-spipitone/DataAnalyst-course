import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns  
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import LabelEncoder #Importiamo la libreria

df_price = pd.read_csv("DataAnalyst-course/Studenti/MaraAntuofermo/Giorno 13/CarPrice_Assignment.csv")
print(df_price.head())

#Convertiamo in Dataset/Excel per leggere meglio i dati
df_price.to_excel("DataAnalyst-course/Studenti/MaraAntuofermo/Giorno 13/CarPrice_Assignment.xlsx", index=False)

#Convertiriamo il numero delle porte della macchina in numeri
def convertdoor(x):
    if x == "four":
        return 4
    else:
        return 2
    
df_price["doornumber"] = df_price["doornumber"].apply(convertdoor)

#Ci permette di convertire la stringa in valore numerico
Le = LabelEncoder()
df_price["cylindernumber"] = Le.fit_transform(df_price["cylindernumber"])

X = df_price[["enginesize", "horsepower"]]
print(X.head())
Y = df_price["price"]

x_train, x_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

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
for feature, coef in zip(features, coefficients):
    print(f"Coefficiente per {feature}: {coef:.2f} € per unità")

print(" INTERPRETAZIONE DEI COEFFICIENTI:")
print("All'aumento della cilindrata, il prezzo aumenta di circa {:.2f} €.".format(
        coefficients[0]))

print(
    "Per ogni cavallo in più, il prezzo aumenta di circa {:.2f} €.".format(
        coefficients[1]
    )
)



plt.figure(figsize=(18, 12))
plt.scatter(y_test, y_pred, alpha=0.7, color="blue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw=2)
plt.xlabel("Prezzi Auto Reali (€)")
plt.ylabel("Prezzi Auto Predetti (€)")
plt.title("Prezzi Reali vs Prezzi Predetti")
plt.grid(True, alpha=0.3)
plt.show()

#Ora possiamo decidere se fare un ciclo While oppure mettere un'istanza specifica a mano