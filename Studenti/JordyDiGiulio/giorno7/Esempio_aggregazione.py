import pandas as pd  # Importa la libreria pandas e la rinomina come pd

df = pd.read_csv(
    r"Esercizi\Giorno 7\vendite.csv"
)  # Legge il file CSV e lo carica in un DataFrame

# Raggruppa i dati per la colonna "Categoria" e applica diverse funzioni di aggregazione
risultato = df.groupby("Categoria").agg(
    {
        "Vendite": [
            "sum",  # Calcola la somma delle vendite per ogni categoria
            "mean",  # Calcola la media delle vendite per ogni categoria
            "std",  # Calcola la deviazione standard delle vendite per ogni categoria
        ],
        "Clienti": [
            "count",  # Conta il numero di righe (clienti) per ogni categoria
            "max",  # Trova il valore massimo di clienti per ogni categoria
        ],
        "Profitto": [
            "min",  # Trova il profitto minimo per ogni categoria
            "max",  # Trova il profitto massimo per ogni categoria
            "mean",  # Calcola la media del profitto per ogni categoria
        ],
    }
)

df = (
    risultato.reset_index()
)  # Reimposta l'indice per ottenere 'Categoria' come colonna normale

df_mobili = df[
    df["Categoria"].isin(["Mobili"])
].reset_index()  # Filtra il DataFrame per la categoria "Mobili" e reimposta l'indice

df_sum_mobili = df_mobili["Vendite"][
    "sum"
].reset_index()  # Estrae la colonna della somma delle vendite per "Mobili" e reimposta l'indice

print(
    "sum mobili:", df_sum_mobili
)  # Stampa la somma delle vendite per la categoria "Mobili"

# print(df_mobili)  # (Opzionale) Stampa il DataFrame filtrato per la categoria "Mobili"
# print(risultato)  # (Opzionale) Stampa il risultato aggregato
