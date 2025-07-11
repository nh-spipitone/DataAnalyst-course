#ESERCIZIO:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns  
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import LabelEncoder       #Importiamo la libreria



df_car_price = pd.read_csv(r"C:\Users\nnngh\Desktop\Corso Data Analyst\DataAnalyst-course\Esercizi\Giorno 13\CarPrice_Assignment.csv")


print(df_car_price.head())




x= df_car_price[["CarName", "fueltype", "horsepower", "enginesize", "cylindernumber", "doornumber"]]
y= df_car_price[["price"]]


categorical_features = x.select_dtypes(
include=["object"]
).columns.tolist()


x_processed = x.copy()

label_encoders = {}

for feature in categorical_features:
    le = LabelEncoder()
    x_processed[feature] = le.fit_transform(x_processed[feature]).astype(str)
    label_encoders[feature] = le




x_train, x_test, y_train, y_test = train_test_split(
    x_processed, y, test_size=0.2, random_state=42
)


model= LinearRegression()
model.fit(x_train, y_train)


y_pred = model.predict(x_test)



print("Valutazione del modello:")
print("RMSE", np.sqrt(mean_squared_error(y_test, y_pred)))
print("MAE", mean_absolute_error(y_test, y_pred))
print("R2", r2_score(y_test, y_pred))




features= x_processed.columns
coefficients = model.coef_
intercept = model.intercept_


print(f"Intercetta: {intercept[0]:.2f} $")





for feature, coef in zip(features, coefficients):
    print (f"Coefficiente per {feature}: {coef[0]:.2f} $ per unità")




print(" INTERPRETAZIONE DEI COEFFICIENTI:")





plt.subplot(1, 2, 1)                                                       # 1 riga, 2 colonne, primo grafico
plt.scatter(y_test, y_pred, alpha=0.7, color="blue")                       # Disegna i punti
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw=2)      # Disegna la retta
plt.xlabel("Prezzi Reali (€)")                   # Etichetta asse x
plt.ylabel("Prezzi Predetti (€)")                # Etichetta asse y
plt.title("Prezzo in funzione dei parametri")     # Titolo del grafico
plt.grid(True, alpha=0.3)                        # Disegna la griglia


plt.tight_layout()      # Ridimensiona automaticamente i grafici
plt.show()              # Visualizza i grafici