# Analisi di base di un dataset di vendite con funzioni, if, while e pandas

# Livello: beginner data analyst – l’obiettivo è prendere dimestichezza con la lettura di file CSV, la gestione del flusso di controllo in Python e le prime operazioni di analisi dati con pandas.
import pandas as pd

# Funzione per caricare i dati
def carica_dati(percorso_file:str) -> pd.DataFrame:
    """
    Carica i dati da un file CSV in un DataFrame pandas.
    
    Args:
        percorso_file (str): Il percorso del file CSV da caricare.
    
    Returns:
        pd.DataFrame: Il DataFrame contenente i dati del file CSV.
    """
    try:
        df = pd.read_csv(percorso_file)
        # Verifica se il DataFrame è completo con le colonne attese
        colonne_attese = ['data', 'prodotto', 'quantita', 'prezzo_unitario']
        if not all(col in df.columns for col in colonne_attese):
            raise ValueError("Il DataFrame non contiene tutte le colonne attese.")
        return df
    except FileNotFoundError:
        print(f"Errore: il file {percorso_file} non è stato trovato.")
        return pd.DataFrame()  # Ritorna un DataFrame vuoto in caso di errore
    except pd.errors.EmptyDataError:
        print(f"Errore: il file {percorso_file} è vuoto.")
        return pd.DataFrame()
    except ValueError as ve:
        print(f"Errore: {ve}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Errore imprevisto: {e}")
        return pd.DataFrame()

# Funzione per calcolare il riepilogo delle vendite    
def riepilogo_vendite(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcola un riepilogo delle vendite per prodotto.
    
    Args:
        df (pd.DataFrame): Il DataFrame contenente i dati delle vendite.
    
    Returns:
        pd.DataFrame: Un DataFrame con il riepilogo delle vendite per prodotto.
    """
    if df.empty:
        return pd.DataFrame()  # Ritorna un DataFrame vuoto se non ci sono dati
    
    df['ricavo'] = df['prezzo_unitario'] * df['quantita']
    quantita_totale = df['quantita'].sum()
    ricavo_totale = df['ricavo'].sum()
    ordine_medio = ricavo_totale / len(df)
    
    return pd.DataFrame({
        'quantita_totale': [quantita_totale],
        'ricavo_totale': [ricavo_totale],
        'ordine_medio': [ordine_medio]
    })

# Funzione per analizzare un prodotto specifico nel DataFrame delle vendite
def cerca_prodotto(df: pd.DataFrame, prodotto: str):
    """
    Cerca un prodotto specifico nel DataFrame delle vendite, se lo trova, stampa quantità totale e ricavo totale.
    Se il prodotto non viene trovato, stampa un messaggio di avviso.
    
    Args:
        df (pd.DataFrame): Il DataFrame contenente i dati delle vendite.
        prodotto (str): Il nome del prodotto da cercare.            
    """
    if df.empty:
        print("Il DataFrame è vuoto. Non ci sono dati da cercare.")
        return
    
    # Verifica se il prodotto è presente nel DataFrame, senza case sensitivity
    lista_prodotti_lower = list(df['prodotto'].str.strip().str.lower()) # Crea una lista di prodotti in minuscolo
    if prodotto.strip().lower() not in lista_prodotti_lower: 
        print(f"Il prodotto '{prodotto}' non è stato trovato nelle vendite.")
        return

    # genera un DataFrame filtrato per il prodotto specificato, senza case sensitivity
    df_prodotto = df[df['prodotto'].str.strip().str.lower() == prodotto.strip().lower()]
    # stampa il riepilogo delle vendite per il prodotto specificato
    print(f"Riepilogo per il prodotto '{prodotto}':")
    print(df_prodotto[['data', 'quantita', 'prezzo_unitario']])
    quantita_totale = df_prodotto['quantita'].sum()
    ricavo_totale = (df_prodotto['prezzo_unitario'] * df_prodotto['quantita']).sum()
    print(f"Quantità totale venduta: {quantita_totale}")
    print(f"Ricavo totale: {ricavo_totale:.2f} euro")

# Funzione per salvare il riepilogo delle vendite in un file CSV
def salva_riepilogo(riepilogo: pd.DataFrame, percorso_file: str):
    """
    Salva il riepilogo delle vendite in un file CSV.
    
    Args:
        riepilogo (pd.DataFrame): Il DataFrame contenente il riepilogo delle vendite.
        percorso_file (str): Il percorso del file CSV in cui salvare il riepilogo.
    """
    try:
        riepilogo.to_csv(percorso_file, index=False)
        print(f"Riepilogo salvato con successo in {percorso_file}.")
    except Exception as e:
        print(f"Errore durante il salvataggio del riepilogo: {e}")

# Funzione principale per eseguire l'analisi delle vendite
def main():
    """
    Funzione principale per eseguire l'analisi delle vendite.
    """

    percorso_file = "/home/giovanni/Programs/Python3/DataAnalyst-course/Esercizi/Giorno 3/vendite.csv" 
    #input("Inserisci il percorso del file CSV: ")
    
    df = carica_dati(percorso_file)
    if df.empty:
        print("Nessun dato disponibile per l'analisi.")
        return
    print("Dati caricati con successo.")
    print("Anteprima dei dati:")
    print(df.head())

    riepilogo = riepilogo_vendite(df)
    if riepilogo.empty:
        print("Nessun riepilogo disponibile.")
    else:
        print("Riepilogo delle vendite:")
        print(riepilogo)
        #salva_riepilogo(riepilogo, "riepilogo_vendite.csv")

    lista_prodotti = df['prodotto'].unique()
    print("Prodotti disponibili:", ", ".join(lista_prodotti))
    while True:
        try:
            # Chiede all'utente il nome del prodotto da cercare
            prodotto = input("Inserisci il nome del prodotto da cercare (o 'esci' per terminare): ").strip()
            if prodotto.lower() == 'esci':
                print("Uscita dalla ricerca dei prodotti.")
                break
            cerca_prodotto(df, prodotto)
        except KeyboardInterrupt:
            print("\nUscita dalla ricerca dei prodotti.")
            break    
        except Exception as e:
            print(f"Errore durante la ricerca del prodotto: {e}")
            continue  # Continua il loop in caso di errore

    print("Analisi delle vendite completata.")


# Esecuzione del programma
# Se il file viene eseguito direttamente, chiama la funzione main
if __name__ == "__main__":
    print("Inizio analisi del file vendite.csv")
    main()
