# Esercizio: "Studiare paga?"
# Hai a disposizione un dataset con 100 osservazioni. Ogni osservazione rappresenta uno studente, con:
# OreStudio: il numero di ore dedicate allo studio prima dell'esame.
# VotoEsame: il voto ottenuto all'esame.
# 🎯 Obiettivo
# Analizzare se esiste una relazione lineare tra le ore di studio e il voto d’esame, utilizzando la regressione lineare semplice.
# rispetto al modello, dimmi il voto finale sapendo che le ore si studio sono pari a 5h

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df_dati = pd.read_csv(r"DataAnalyst-course\Studenti\NicoloGibroni\Giorno12\dataset_regressione.csv")

x = df_dati[["OreStudio"]].values
y = df_dati[["VotoEsame"]].values

X_train, X_test, y_train, y_test = (train_test_split(x, y, test_size=0.2, random_state=42))

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Coefficiente (pendenza): {model.coef_[0][0]:.3f}")
print(f"Intercetta: {model.intercept_[0]:.3f}")
print(f"R² sul test set: {model.score(X_test, y_test):.3f}")
print(f"Previsione del voto per 5 ore di studio: {model.predict([[5]])[0][0]:.2f}") # voto associato alle 5 ore di sonno
plt.scatter(x, y, label="Dati")
X_line = x.copy()
X_line.sort(axis=0)
y_line = model.predict(X_line)
plt.plot(X_line, y_line, color="red", label="Regr. Lineare")
plt.xlabel("OreStudio")
plt.ylabel("VotoEsame")
plt.title("Regressione Lineare")
plt.legend()
plt.show() 

