import pandas as pd
import matplotlib.pyplot as plt

def carica_dati(percorso: str) -> pd.DataFrame:
    df = pd.read_csv(percorso)
    return df

df = carica_dati("Esercizi\\Giorno 4\\ordini.csv")
print(df.head())

df["Totale"] = df["Quantità"] * df["Prezzo_unitario"]

for i, ordine in df.iterrows():
    lista_non_spediti = []

    if not ordine["Spedito"]: lista_non_spediti.append(
        (
            ordine["OrdineID"], 
            ordine["Data"], 
            ordine["Cliente"], 
            ordine["Prodotto"], 
            ordine["Totale"]
        )
    )


print(lista_non_spediti)

fatturato_clienti = df.groupby("Cliente")["Totale"].sum().sort_values(ascending = False)
print(fatturato_clienti)

prodotto_piu_venduto = df.groupby("Prodotto")["Quantità"].sum().idxmax()
print(prodotto_piu_venduto)

fatturato_giornaliero = (df.groupby("Data")["Totale"].sum().reset_index())
print(fatturato_giornaliero)

plt.figure(figsize = (10, 6))
plt.bar(fatturato_giornaliero["Data"], fatturato_giornaliero["Totale"], color = "skyblue")
plt.xlabel("Data", fontsize = 12)
plt.ylabel("Fatturato (€)", fontsize = 12)
plt.title("Fatturato giornaliero", fontsize = 16)
plt.tight_layout()
plt.show()

media_prezzo_per_prodotto = (df.groupby("Prodotto")["Prezzo_unitario"].mean().reset_index())
print(media_prezzo_per_prodotto)