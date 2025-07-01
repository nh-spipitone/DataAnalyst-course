import pandas as pd 
import matplotlib.pyplot as plt 

def carica_dati(percorso: str) -> pd.DataFrame:
    df = pd.read_csv(percorso)
    return df

df = carica_dati("Esercizi\\Giorno 5\\vendite.csv")
print(df.head())


fatturato_giornaliero = df.groupby("Data")["Prezzo_unitario"].sum().reset_index()
print(fatturato_giornaliero)

df["Fatturato"] = df["Quantità"] * df["Prezzo_unitario"]
print(df.head())

fatturato_totale_prodotto = df.groupby("Prodotto")["Prezzo_unitario"].sum().reset_index()
print(df.head())

plt.figure(figsize = (10, 8))
fatturato_totale_prodotto = df.groupby("Prodotto")["Prezzo_unitario"].sum()
fatturato_totale_prodotto.plot(kind = "bar", color = "skyblue")
plt.title("Fatturato totale per ogni prodotto", fontsize = 16)
plt.xlabel("Prodotto", fontsize = 14)
plt.ylabel("Fatturato (€)", fontsize = 14)
plt.tight_layout()
plt.show()

prodotto_piu_venduto = fatturato_totale_prodotto.idxmax()
fatturato_piu_venduto = fatturato_totale_prodotto.max()
print(f"Prodotto più venduto: {prodotto_piu_venduto} con fatturato di {fatturato_piu_venduto}€")