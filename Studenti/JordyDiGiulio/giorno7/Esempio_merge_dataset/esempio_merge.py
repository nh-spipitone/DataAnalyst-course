import pandas as pd

clienti = pd.read_csv(
    r"Esercizi\Giorno 7\Esempio_merge_dataset\clienti.csv"
)  # Legge il file CSV e lo carica in un DataFrame

ordini = pd.read_csv(
    r"Esercizi\Giorno 7\Esempio_merge_dataset\ordini.csv"
)  # Legge il file CSV degli ordini e lo carica in un DataFrame


df_merged = pd.merge(
    clienti,
    ordini,
    how="left",
    left_on=["ID_Cliente"],
    right_on=["Cliente_ID"],
    suffixes=("_Cliente", "_Ordine"),
)

print("DataFrame unito:\n", df_merged)  # Stampa il DataFrame unito
