import pandas as pd

def carica_dati(percorso: str) -> pd.DataFrame:
    df = pd.read_csv(percorso)
    return df

def riepilogo_vendite(df: pd.DataFrame) -> pd.DataFrame:
    totale_quantita = df["quantita"].sum()
    df["ricavi"] = df["quantita"] * df["prezzo_unitario"]
    totale_ricavi = df["ricavi"].sum()
    ordine_medio = totale_ricavi / len(df)
    
     

    return pd.DataFrame({"totale_quantita": [totale_quantita], "totale_ricavi": [totale_ricavi], "ordine_medio": [ordine_medio]})

#2.3

def cerca_prodotto(nome_prodotto : str, df : pd.DataFrame):
    k = 0
    for prodotto in df["prodotto"]:

        if nome_prodotto.lower() == prodotto.lower():
            print(f"prodotto non trovato: {prodotto}")
            print(f"quantita: {df["quantita"][k]} prezzo unitario {df["prezzo_unitario"][k]}")
            k += 1

cerca_prodotto("penna", carica_dati("Esercizi\\Giorno 3\\vendite.csv"))





