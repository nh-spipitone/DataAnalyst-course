import pandas as pd




def carica_dati(percorso: str) -> pd.DataFrame:
    
    df = pd.read_csv(percorso)
    
    return df



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



def cerca_prodotto(nome_prodotto: str, df: pd.DataFrame):
    
    contatore = 0
    
    for prodotto in df["prodotto"]:
        
        if nome_prodotto.lower() == prodotto.lower():
            
            print(f"Prodotto trovato: {prodotto}")
            
            print(
                f"Quantità: {df['quantita'][contatore]} Prezzo Unitario:{df['prezzo_unitario'][contatore]}"
            )
        
        contatore += 1


# Versione più efficiente della funzione di ricerca prodotto
def cerca_prodotto_efficiente(nome_prodotto: str, df: pd.DataFrame):
    
    for index, row in df.iterrows():
       
        prodotto = row["prodotto"]
        
        if nome_prodotto.lower() == prodotto.lower():
            
            print(f"Prodotto trovato: {prodotto}")
            
            print(
                f"Quantità: {row['quantita']} Prezzo Unitario:{row['prezzo_unitario']}"
            )



def salva_riepilogo(riepilogo: pd.DataFrame, percorso: str):
    
    riepilogo.to_excel(percorso, index=False)
    
    print(f"Riepilogo vendite salvato in {percorso}")



df_vendite = carica_dati(r"Esercizi\Giorno 3\vendite.csv")


while True:
    
    scelta = input(
        "Vuoi vedere il riepilogo delle vendite (1) o cercare un prodotto (2)? "
    )
    
    if scelta == "1":
        
        riepilogo = riepilogo_vendite(df_vendite)
        
        print(riepilogo)
        
        salva_riepilogo(riepilogo, "riepilogo_vendite.xlsx")
    
    elif scelta == "2":
        
        nome_prodotto = input("Inserisci il nome del prodotto da cercare:")
        
        cerca_prodotto(nome_prodotto, df_vendite)
    
    else:
        
        print("Scelta non valida. Riprova.")
    
    continua = input("Vuoi continuare a cercare? (s/n): ")
    
    if continua.lower() != "s" and continua.lower() != "si":
        break