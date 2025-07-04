import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"DataAnalyst-course\Studenti\NicoloGibroni\Giorno6\googleplaystore (1).csv")
# Esercizio: Analisi delle app per categoria e numero di download
# 🎯 Obiettivo:
# Il tuo obiettivo è analizzare il numero di download per categoria di app, e calcolare la media delle valutazioni per ciascuna categoria. Successivamente, crea un grafico a barre per visualizzare i download totali per categoria.
# 📋 Istruzioni per la consegna:
# Carica il dataset:
# Usa il file googleplaystore.csv per caricare i dati che contengono informazioni sulle app disponibili su Google Play Store.
# Prepara i dati:

df["Installs"] = df["Installs"].str.replace(",","").str.replace("+","")
df["Installs"] = pd.to_numeric(df["Installs"])
df["Reviews"] = pd.to_numeric(df["Reviews"])
df = df.dropna(subset=["Installs", "Rating"])
installs = df.groupby("Category")["Installs"].sum().sort_values(ascending=False)
ratings = df.groupby("Category")["Rating"].mean()
installs.plot(kind="bar", figsize=(12,6), title="Totale Installazioni per Categoria")
plt.xlabel("Category")
plt.ylabel("Total Installs")
plt.tight_layout()
plt.show()

reviews = df.groupby("Category")["Reviews"].mean().sort_values(ascending=False)
reviews.plot(kind="bar", figsize=(12,6), title="Media recensione per Categoria")
plt.show()