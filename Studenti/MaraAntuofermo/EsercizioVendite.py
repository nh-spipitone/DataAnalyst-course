#Esercizio: Analisi di base di un dataset di vendite con funzioni, if, while e pandas

import pandas as pd

# 2.1 
def carica_dati(percorso:str) -> pd.DataFrame:
    df=pd.read_csv(percorso)
    return df
# 2.2 
def riepilogo_vendite(df: pd.DataFrame) -> pd.DataFrame:
    totale_quantita= df["quantita"].sum()
    df["ricavo"]= df["quantita"] * df["prezzo_unitario"]
    totale_ricavi =  df["ricavo"].sum()
    ordine_medio = totale_ricavi / len(df)

    return pd.DataFrame ({"totale_quantita": [totale_quantita], "totale_ricavi": [totale_ricavi], "ordine_medio": [ordine_medio]})

# 2.3 
def cerca_prodotto(nome_prodotto:str , df:pd.DataFrame): 
    if nome_prodotto in df["prodotto"]:
        sub_df = df.loc[df["prodotto"], ["quantita", "prezzo_unitario"]]
        sub_df 


while True: 


