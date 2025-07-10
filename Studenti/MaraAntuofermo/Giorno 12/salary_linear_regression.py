import numpy as np  # Importa la libreria numpy per operazioni numeriche
import pandas as pd  # Importa pandas per la gestione dei dati
from sklearn.model_selection import (
    train_test_split,
)  # Importa la funzione per suddividere il dataset
from sklearn.linear_model import (
    LinearRegression,
)  # Importa il modello di regressione lineare
import matplotlib.pyplot as plt  # Importa matplotlib per la visualizzazione grafica


df_salary = pd.read_csv(
    r"Esercizi\Giorno 12\Salary_dataset.csv"
)  # Legge il file CSV in un DataFrame

print(df_salary.head())  # Mostra le prime righe del DataFrame per verifica

x = df_salary[
    ["YearsExperience"]
].values  # Estrae la colonna 'YearsExperience' come array numpy bidimensionale
y = df_salary[["Salary"]].values  # Estrae la colonna 'Salary

x_train, x_test, y_train, y_test = (
    train_test_split(  # Divide i dati in train e test set
        x, y, test_size=0.2, random_state=42
    )
)

model = LinearRegression()  # Crea un oggetto modello di regressione lineare
model.fit(x_train, y_train)  # Allena il modello sui dati di training
print(
    "Score del modello:", model.score(x_test, y_test)
)  # Stampa il punteggio del modello

plt.scatter(x, y, label="Dati Salario")  # Crea uno scatter plot dei dati originali
x_line = x.copy()  # Copia i valori di x per la linea di regressione
x_line.sort(axis=0)  # Ordina i valori di x per una linea più
y_line = model.predict(x_line)  # Calcola i valori previsti dal modello
plt.plot(
    x_line, y_line, color="red", label="Regr. Lineare"
)  # Disegna la retta di regressione
plt.xlabel("Anni di Esperienza")  # Etichetta asse x
plt.ylabel("Salario (in $)")  # Etichetta asse y
plt.title(
    "Regressione Lineare del Salario in base agli Anni di Esperienza"
)  # Titolo del grafico
plt.legend()  # Mostra la legenda

plt.grid(True)  # Mostra la griglia sul grafico
plt.show()  # Visualizza il grafico
