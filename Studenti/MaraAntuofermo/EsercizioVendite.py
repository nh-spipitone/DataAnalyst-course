# Esercizio: Analisi di base di un dataset di vendite con funzioni, if, while e pandas

import pandas as pd


# 2.1
def carica_dati(percorso: str) -> pd.DataFrame:
    df = pd.read_csv(percorso)
    return df


# 2.2
def riepilogo_vendite(df: pd.DataFrame) -> pd.DataFrame:
    totale_quantita = df["quantita"].sum()
    df["ricavo"] = df["quantita"] * df["prezzo_unitario"]
    totale_ricavi = df["ricavo"].sum()
    ordine_medio = totale_ricavi / len(df)

    return pd.DataFrame(
        {
            "totale_quantita": [totale_quantita],
            "totale_ricavi": [totale_ricavi],
            "ordine_medio": [ordine_medio],
        }
    )


# 2.3
def cerca_prodotto(nome_prodotto: str, df: pd.DataFrame):
    contatore = 0
    for prodotto in df["prodotto"]:

        if nome_prodotto.lower() == prodotto.lower():
            print(f"Prodotto trovato: {prodotto}")
            print(f"Quantità: {df['quantita'][contatore]} Prezzo Unitario:{df['prezzo_unitario'][contatore]}")
        contatore += 1


cerca_prodotto("Penna", carica_dati("Esercizi\\Giorno 3\\vendite.csv"))
