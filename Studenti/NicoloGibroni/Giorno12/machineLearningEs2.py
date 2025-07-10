# Il dataset Iris contiene osservazioni su tre specie di fiori: setosa, versicolor e virginica. Ogni fiore è descritto da 4 misurazioni in cm:
# sepal length (cm) – lunghezza del sepalo
# sepal width (cm) – larghezza del sepalo
# petal length (cm) – lunghezza del petalo
# petal width (cm) – larghezza del petalo
# 🎯 Obiettivo
# Analizzare la relazione tra la lunghezza del sepalo e la lunghezza del petalo, utilizzando la regressione lineare semplice. 
# E poi tra larghezza del sepalo e lunghezza del petalo, dire quale tra le due variabili, lunguezza del sepalo e larghezza del sepalo, migliora la previsione della lunghezza del petalo


# imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# csv salvato in df_dati
df_dati = pd.read_csv(r"DataAnalyst-course\Studenti\NicoloGibroni\Giorno12\iris_dataset.csv")

# x e y sono array 2d delle 2 colonne
x = df_dati[["sepal length (cm)"]].values
y = df_dati[["petal length (cm)"]].values

# divide i dati in 2 parti. test_size=0.2 (Usa il 20% dei dati per il test, e il restante 80% per il training)
X_train, X_test, y_train, y_test = (train_test_split(x, y, test_size=0.2, random_state=42))

# diciamo che vogliamo usare un modello di regressione lineare
model = LinearRegression()
# è l'addestramento
model.fit(X_train, y_train)

# i vari print
print(f"Coefficiente (pendenza): {model.coef_[0][0]:.3f}")
print(f"Intercetta: {model.intercept_[0]:.3f}")
print(f"R² sul test set: {model.score(X_test, y_test):.3f}")

# griglia per mettere 2 grafici nella stessa finestra
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# fa uno scatter nella posizione sinistra della griglia
axes[0].scatter(x, y, label="Dati")
# copia dell'array x e ordina
X_line = x.copy()
X_line.sort(axis=0)
# Calcola le previsioni del modello per ogni valore in X_line
# y_line contiene i voti previsti dal modello, dati gli x ordinati
y_line = model.predict(X_line)

# Disegna la linea di regressione (cioè la retta trovata dal modello)
axes[0].plot(X_line, y_line, color="red", label="Regr. Lineare")

# varie info descrittive
axes[0].set_xlabel("sepal length (cm)")
axes[0].set_ylabel("petal length (cm)")
axes[0].set_title("Regressione Lineare")
axes[0].legend()



x = df_dati[["sepal width (cm)"]].values
y = df_dati[["petal length (cm)"]].values

X_train, X_test, y_train, y_test = (train_test_split(x, y, test_size=0.2, random_state=42))

model.fit(X_train, y_train)

axes[1].scatter(x, y, label="Dati")
X_line = x.copy()
X_line.sort(axis=0)
y_line = model.predict(X_line)

print(f"Coefficiente (pendenza): {model.coef_[0][0]:.3f}")
print(f"Intercetta: {model.intercept_[0]:.3f}")
print(f"R² sul test set: {model.score(X_test, y_test):.3f}")

axes[1].plot(X_line, y_line, color="red", label="Regr. Lineare")

axes[1].set_xlabel("sepal width (cm)")
axes[1].set_ylabel("petal length (cm)")
axes[1].set_title("Regressione Lineare")
axes[1].legend()

plt.tight_layout()
plt.show() 
