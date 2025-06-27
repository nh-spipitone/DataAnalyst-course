# Esercizio: Analisi di base di un dataset di vendite con funzioni, if, while e pandas

# Importa la libreria pandas per la manipolazione dei dati
import pandas as pd


# 2.1
# Definisce una funzione per caricare i dati da un file CSV
def carica_dati(percorso: str) -> pd.DataFrame:
    # Legge il file CSV dal percorso specificato e lo carica in un DataFrame
    df = pd.read_csv(percorso)
    # Restituisce il DataFrame caricato
    return df


# 2.2
# Definisce una funzione per calcolare il riepilogo delle vendite
def riepilogo_vendite(df: pd.DataFrame) -> pd.DataFrame:
    # Calcola la somma totale delle quantità vendute
    totale_quantita = df["quantita"].sum()
    # Crea una nuova colonna "ricavo" moltiplicando quantità per prezzo unitario
    df["ricavo"] = df["quantita"] * df["prezzo_unitario"]
    # Calcola la somma totale dei ricavi
    totale_ricavi = df["ricavo"].sum()
    # Calcola l'ordine medio dividendo i ricavi totali per il numero di righe
    ordine_medio = totale_ricavi / len(df)

    # Restituisce un DataFrame con i risultati del riepilogo
    return pd.DataFrame(
        {
            "totale_quantita": [totale_quantita],
            "totale_ricavi": [totale_ricavi],
            "ordine_medio": [ordine_medio],
        }
    )


# 2.3
# Definisce una funzione per cercare un prodotto nel DataFrame (versione con contatore)
def cerca_prodotto(nome_prodotto: str, df: pd.DataFrame):
    # Inizializza un contatore per accedere agli indici delle righe
    contatore = 0
    # Itera attraverso tutti i prodotti nella colonna "prodotto"
    for prodotto in df["prodotto"]:
        # Confronta il nome del prodotto cercato con quello corrente (case-insensitive)
        if nome_prodotto.lower() == prodotto.lower():
            # Stampa il nome del prodotto trovato
            print(f"Prodotto trovato: {prodotto}")
            # Stampa quantità e prezzo unitario usando il contatore come indice
            print(
                f"Quantità: {df['quantita'][contatore]} Prezzo Unitario:{df['prezzo_unitario'][contatore]}"
            )
        # Incrementa il contatore per la prossima iterazione
        contatore += 1


# Versione più efficiente della funzione di ricerca prodotto
def cerca_prodotto_efficiente(nome_prodotto: str, df: pd.DataFrame):
    # Itera attraverso le righe del DataFrame usando iterrows()
    for index, row in df.iterrows():
        # Ottiene il nome del prodotto dalla riga corrente
        prodotto = row["prodotto"]
        # Confronta il nome del prodotto cercato con quello corrente (case-insensitive)
        if nome_prodotto.lower() == prodotto.lower():
            # Stampa il nome del prodotto trovato
            print(f"Prodotto trovato: {prodotto}")
            # Stampa quantità e prezzo unitario dalla riga corrente
            print(
                f"Quantità: {row['quantita']} Prezzo Unitario:{row['prezzo_unitario']}"
            )


# Definisce una funzione per salvare il riepilogo in un file Excel
def salva_riepilogo(riepilogo: pd.DataFrame, percorso: str):
    # Salva il DataFrame in un file Excel senza includere l'indice
    riepilogo.to_excel(percorso, index=False)
    # Stampa un messaggio di conferma
    print(f"Riepilogo vendite salvato in {percorso}")


# Carica i dati delle vendite dal file CSV
df_vendite = carica_dati(r"Esercizi\Giorno 3\vendite.csv")

# Inizia un ciclo infinito per il menu interattivo
while True:
    # Chiede all'utente di scegliere un'opzione
    scelta = input(
        "Vuoi vedere il riepilogo delle vendite (1) o cercare un prodotto (2)? "
    )
    # Se l'utente sceglie opzione 1
    if scelta == "1":
        # Genera il riepilogo delle vendite
        riepilogo = riepilogo_vendite(df_vendite)
        # Stampa il riepilogo
        print(riepilogo)
        # Salva il riepilogo in un file Excel
        salva_riepilogo(riepilogo, "riepilogo_vendite.xlsx")
    # Se l'utente sceglie opzione 2
    elif scelta == "2":
        # Chiede all'utente il nome del prodotto da cercare
        nome_prodotto = input("Inserisci il nome del prodotto da cercare:")
        # Cerca il prodotto nel DataFrame
        cerca_prodotto(nome_prodotto, df_vendite)
    # Se l'utente inserisce un'opzione non valida
    else:
        # Stampa un messaggio di errore
        print("Scelta non valida. Riprova.")
    # Chiede all'utente se vuole continuare
    continua = input("Vuoi continuare a cercare? (s/n): ")
    # Se la risposta non è "s" o "si", esce dal ciclo
    if continua.lower() != "s" and continua.lower() != "si":
        break
