import pandas as pd

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
