import pandas as pd  # Importa la libreria pandas per la manipolazione dei dati

df = pd.read_csv(
    r"Esercizi\Giorno 7\dati_temporali.csv"
)  # Legge il file CSV e lo carica in un DataFrame


def calcola_categoria(valore):  # Definisce una funzione per categorizzare i valori
    if valore < 100:  # Se il valore è minore di 100
        return "Basso"  # Restituisce "Basso"
    elif valore < 500:  # Se il valore è minore di 500
        return "Medio"  # Restituisce "Medio"
    else:  # Altrimenti
        return "Alto"  # Restituisce "Alto"


df["Categoria"] = df["Valore"].apply(
    calcola_categoria
)  # Applica la funzione ai valori della colonna "Valore" e crea una nuova colonna "Categoria"

# print(df)  # (Opzionale) Stampa il DataFrame risultante

df_finestra = df.set_index(
    "Data"
)  # Imposta la colonna "Data" come indice del DataFrame
medie_mobili = (
    df_finestra["Valore"].rolling(window=3).mean().dropna()
)  # Calcola la media mobile su 7 giorni e rimuove i valori NaN
print(medie_mobili)  # Stampa le medie mobili calcolate
