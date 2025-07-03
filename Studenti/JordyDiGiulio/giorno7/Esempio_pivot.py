import pandas as pd  # Importa la libreria pandas e la rinomina come pd

df = pd.read_csv(
    r"Esercizi\Giorno 7\ordini.csv"
)  # Legge il file CSV e lo carica in un DataFrame

tabella_pivot = df.pivot_table(
    values="Vendite",  # Specifica la colonna da aggregare (Vendite)
    index=[
        "Regione",
        "Città",
    ],  # Indica le colonne da usare come indici (righe) nella tabella pivot
    columns="Prodotto",  # Indica la colonna da usare come colonne nella tabella pivot
    aggfunc="sum",  # Specifica la funzione di aggregazione (somma)
    fill_value=0,  # Sostituisce i valori mancanti con 0
)

print(tabella_pivot)  # Stampa la tabella pivot creata
tabella_pivot.to_excel(
    r"Esercizi\Giorno 7\tabella_pivot.xlsx", index=True
)  # Salva la tabella pivot in un file Excel, mantenendo gli indici
