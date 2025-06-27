import pandas as pd

def carica_dati (percorso:str) -> pd.DataFrame:
    df=pd.read_csv(percorso)
    return df

def riepilogo_vendite(df: pd.DataFrame) -> pd.DataFrame:
    totale_quantita= df["quantita"].sum()
    df["ricavo"]= df["quantita"]*df["prezzo_unitario"]
    totale_ricavi= df["ricavo"].sum()
    ordine_medio= totale_ricavi / len(df)

    return pd.DataFrame ({"totale_quantita":[totale_quantita],"totale_ricavi":[totale_ricavi], "ordine_medio":[ordine_medio]})

def cerca_prodotto(nome_prodotto: str, df: pd.DataFrame):
    for index, row in df.iterrows():
        if nome_prodotto.lower() == row["prodotto"].lower():
            print(f"Prodotto trovato: {row["prodotto"]}\nQuantità: {row['quantita']} Prezzo Unitario: {row['prezzo_unitario']}")


# def cerca_prodotto(nome_prodotto: str, df: pd.DataFrame):
#     k = 0
#     for prodotto in df["prodotto"]:
#         if nome_prodotto.lower() == prodotto.lower():
#             print(f"Prodotto trovato: {prodotto}\nQuantità: {df['quantita'][k]} Prezzo Unitario: {df['prezzo_unitario'][k]}")
#         k += 1

def salva_riepilogo(riepilogo: pd.DataFrame, percorso: str):
    riepilogo.to_csv(percorso, index = False)
    print(f"Riepilogo salvato in {percorso}")

df = carica_dati("DataAnalyst-course\\Esercizi\\Giorno 3\\vendite.csv")

while True:
    scelta = input("Vuoi vedere il riepilogo delle vendite (1) o cercare un prodotto (2)? ")

    if scelta == "1":
        riepilogo = riepilogo_vendite(df)
        print(riepilogo)
        salva_riepilogo(riepilogo, "riepilogo_vendite.csv1")
    elif scelta == "2":
        nome_prodotto = input("Inserisci il nome del prodotto da cercare: ")
        cerca_prodotto(nome_prodotto, df)
    else:
        print("Scelta non valida. Riprova.")

    continua = input("Vuoi continuare? (s/n): ")
    if continua.lower() != "s": break