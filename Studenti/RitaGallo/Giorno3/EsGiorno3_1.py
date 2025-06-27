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



def cerca_prodotto_efficiente(nome_prodotto : str, df : pd.DataFrame):
    
    for index, row in df.iterrows():
        prodotto = row["prodotto"]
        if nome_prodotto.lower() == prodotto.lower():
            print(f"prodotto non trovato: {prodotto}")
            print(f"quantita: {row["quantita"]} prezzo unitario {row["prezzo_unitario"]}")
            
def salva_riepilogo(riepilogo: pd.DataFrame, percorso: str):
    riepilogo.to_excel(percorso, index=False)
    print(f"riepilogo vendite salvato in {percorso}")

df_vendite = carica_dati(r"Esercizi\Giorno 3\vendite.csv")

while True:
    scelta = input("vuoi vedere il riepilogo delle vendite (1) o cercare un prodotto (2)?")
    if scelta == 1:
        riepilogo = riepilogo_vendite(df_vendite)
        print(riepilogo)
        salva_riepilogo(riepilogo, "riepilogo_vendite.xlsx")
    elif scelta == "2":
        nome_prodotto = input("inserisci il nome del prodotto da cercare:")
        cerca_prodotto(nome_prodotto, df_vendite)
    else:
        print("scelta non valida")
    continua = input("vuoi continuare a cercare? (s/n): ")
    if continua.lower() != "s" and continua.lower() != "si":
        break
        

cerca_prodotto("penna", carica_dati("Esercizi\\Giorno 3\\vendite.csv"))
