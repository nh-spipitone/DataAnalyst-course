import pandas as pd  # Importa la libreria pandas per la manipolazione dei dati
import matplotlib.pyplot as plt  # Importa matplotlib per la creazione di grafici

df = pd.read_csv(
    r"DataAnalyst-course/Esercizi/Giorno 4/ordini.csv"
)  # Legge il file CSV e lo carica in un DataFrame

print(df.head())  # Stampa le prime 5 righe del DataFrame per una rapida ispezione

df["Totale"] = (
    df["Quantità"] * df["Prezzo_unitario"]
)  # Crea una nuova colonna 'Totale' calcolando quantità * prezzo unitario

lista_non_spediti = []  # Inizializza una lista vuota per gli ordini non spediti
for i, ordine in df.iterrows():  # Itera su ogni riga del DataFrame
    if not ordine["Spedito"]:  # Se l'ordine non è stato spedito
        lista_non_spediti.append(
            (
                ordine["OrdineID"],
                ordine["Data"],
                ordine["Cliente"],
                ordine["Prodotto"],
                ordine["Totale"],
            )
        )  # Aggiunge le info dell'ordine alla lista

print(lista_non_spediti)  # Stampa la lista degli ordini non spediti

fatturato_clienti = (
    df.groupby("Cliente")["Totale"].sum().sort_values(ascending=False)
)  # Calcola il fatturato totale per cliente e lo ordina in modo decrescente

print(fatturato_clienti)  # Stampa il fatturato per cliente

prodotto_più_venduto = (
    df.groupby("Prodotto")["Quantità"].sum().idxmax()
)  # Trova il prodotto più venduto in base alla quantità

print(prodotto_più_venduto)  # Stampa il nome del prodotto più venduto

# calcola fatturato giornaliero
fatturato_giornaliero = (
    df.groupby("Data")["Totale"].sum().reset_index()
)  # Calcola il fatturato totale per ogni data

print(fatturato_giornaliero)  # Stampa il fatturato giornaliero

# plot del fatturato giornaliero
plt.figure(figsize=(10, 8))  # Imposta la dimensione della figura del grafico
plt.bar(
    fatturato_giornaliero["Data"], fatturato_giornaliero["Totale"], color="skyblue"
)  # Crea un grafico a barre del fatturato giornaliero
plt.title("Fatturato Giornaliero", fontsize=16)  # Imposta il titolo del grafico
plt.xlabel("Data", fontsize=12)  # Imposta l'etichetta dell'asse x
plt.ylabel("Fatturato (€)", fontsize=12)  # Imposta l'etichetta dell'asse y
plt.tight_layout()  # Ottimizza il layout del grafico
plt.show()  # Mostra il grafico

media_prezzoXprodotto = (
    df.groupby("Prodotto")["Prezzo_unitario"].mean().reset_index()
)  # Calcola il prezzo medio unitario per ogni prodotto

print(media_prezzoXprodotto)  # Stampa la tabella dei prezzi medi per prodotto
