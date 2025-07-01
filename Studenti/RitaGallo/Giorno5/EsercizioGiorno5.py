# Esercizio: Analisi delle vendite con pandas e matplotlib

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"DataAnalyst-course\Esercizi\Giorno 5\vendite.csv")
print(df.head())

df["Fatturato"] = df["Quantità"] * df["Prezzo_unitario"]
print(df.head)

fatturato_giornaliero = df.groupby("Data")["Prezzo_unitario"].sum().reset_index()
fatturato_totale_prodotto = df.groupby("Prodotto")["Prezzo_unitario"].sum().reset_index()
print(fatturato_totale_prodotto)

fatturato_totale_prodotto = df.groupby("Prodotto")["Fatturato"].sum()

plt.figure(figsize=(10, 8))
fatturato_totale_prodotto.plot(kind = "bar", color = "skyblue")
plt.title("Fatturato totale per ogni prodotto", fontsize = 16)
plt.xlabel("Prodotto", fontsize = 12)
plt.ylabel("Fatturato in euro", fontsize = 14)
plt.tight_layout()
plt.show()

prodotto_piu_venduto = fatturato_totale_prodotto.idmax()
fatturato_piu_venduto = fatturato_totale_prodotto.max()
print(f"il prodotto che ha generato il fatturato piu alto è {prodotto_piu_venduto} con un fatturato di {fatturato_piu_venduto} euro.")
