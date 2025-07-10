import numpy as np  # Importa la libreria numpy per operazioni numeriche
import pandas as pd  # Importa pandas per la gestione dei dati
from sklearn.model_selection import (
    train_test_split,
)  # Importa la funzione per suddividere il dataset
from sklearn.linear_model import (
    LinearRegression,
)  # Importa il modello di regressione lineare
import matplotlib.pyplot as plt  # Importa matplotlib per la visualizzazione grafica

df_dati = pd.read_csv(
    r"Esercizi\Giorno 12\linear_regression_dataset.csv"
)  # Legge il file CSV in un DataFrame

x = df_dati[
    ["Feature"]
].values  # Estrae la colonna 'Feature' come array numpy bidimensionale
y = df_dati[
    ["Target"]
].values  # Estrae la colonna 'Target' come array numpy bidimensionale

X_train, X_test, y_train, y_test = (
    train_test_split(  # Divide i dati in train e test set
        x, y, test_size=0.2, random_state=42
    )
)

model = LinearRegression()  # Crea un oggetto modello di regressione lineare
model.fit(X_train, y_train)  # Allena il modello sui dati di training

print(
    f"Coefficiente (pendenza): {model.coef_[0][0]:.3f}"
)  # Stampa il coefficiente della retta
print(f"Intercetta: {model.intercept_[0]:.3f}")  # Stampa l'intercetta della retta
print(
    f"R² sul test set: {model.score(X_test, y_test):.3f}"
)  # Stampa il punteggio R² sul test set

plt.scatter(x, y, label="Dati")  # Crea uno scatter plot dei dati originali
X_line = x.copy()  # Copia i valori di x per la linea di regressione
X_line.sort(axis=0)  # Ordina i valori di x per una linea più liscia
y_line = model.predict(X_line)  # Calcola i valori previsti dal modello
plt.plot(
    X_line, y_line, color="red", label="Regr. Lineare"
)  # Disegna la retta di regressione
plt.xlabel("Feature")  # Etichetta asse x
plt.ylabel("Target")  # Etichetta asse y
plt.title("Regressione Lineare")  # Titolo del grafico
plt.legend()  # Mostra la legenda
plt.show()  # Visualizza il grafico
