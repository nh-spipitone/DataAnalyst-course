# Esercizio 1: Analisi passeggeri Titanic + Istogramma dell'età
# Obiettivo: Analizzare e visualizzare la distribuzione dell’età dei passeggeri del Titanic.
# Istruzioni:
# Carica il dataset titanic.csv.
# Rimuovi le righe con età mancante (Age).
# Calcola:
# L’età media
# Il numero totale di passeggeri
# Crea un istogramma dell’età (Age) con matplotlib.pyplot.hist().

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'DataAnalyst-course\Studenti\NicoloGibroni\Giorno5\titanic.csv')

df = df.dropna(subset=["Age"]) #droppa i record con age vuota

# print(df["Age"].mean())
# print(len(df))
# plt.hist(df["Age"], edgecolor = "black")
# plt.title("Distribuzione età")
# plt.xlabel("Età")
# plt.ylabel("Numero passeggeri")
# plt.show()


# Esercizio 2: Bar plot sopravvissuti per sesso
# Obiettivo: Confrontare il numero di sopravvissuti per genere.
# Istruzioni:
# Usa ancora titanic.csv.
# Raggruppa per Sex e Survived, poi conta quanti passeggeri ci sono per ogni gruppo.
# Trasforma i dati in un DataFrame adatto a un bar plot (es. pivot con unstack()).
# Visualizza i risultati con un grafico a barre (.plot(kind='bar')).


#non funziona sta roba sotto
gruppo = df.groupby(["Sex","Survived"]).size()
tabella = gruppo.unstack()
tabella.plot(kind="bar", stacked=True)
plt.title("Distribuzione morti per sesso")
plt.xlabel("Sesso")
plt.ylabel("n passeggeri")
plt.grid(True)
plt.tight_layout()
plt.show()