# Esercizio avanzato: Analisi ordini di un e-commerce

# Hai a disposizione un file ordini.csv che contiene i dati di un piccolo 
# e-commerce nell’ultimo mese. Ogni riga rappresenta un ordine ricevuto.

# Punti della consegna
# Carica il file ordini.csv in un DataFrame Pandas e visualizza le prime 5 righe.
# Aggiungi una colonna “Totale” calcolando per ogni ordine Quantità * Prezzo_unitario.
# Filtra gli ordini che NON sono ancora stati spediti e stampa la lista (con Data, Cliente, Prodotto e Totale).
# Calcola il fatturato totale per ogni cliente (somma dei Totali) e ordina la classifica decrescente.
# Trova il prodotto più venduto in termini di quantità totale.
# (Extra) Trova per ogni giorno il fatturato giornaliero (anche con un grafico a barre).
# (Extra) Calcola la media del prezzo unitario per ogni prodotto.

import pandas as pd

# Carica il file ordini.csv in un DataFrame Pandas e visualizza le prime 5 righe.
df = pd.read_csv('/home/giovanni/Programs/Python3/DataAnalyst-course/Esercizi/Giorno 4/ordini.csv')
print("Prime 5 righe del DataFrame:")
print(df.head())

# Aggiungi una colonna “Totale” calcolando per ogni ordine Quantità * Prezzo_unitario.
df['Totale'] = df['Quantità'] * df['Prezzo_unitario']
print("\nDataFrame con la colonna 'Totale' aggiunta:")
print(df.head())

# Filtra gli ordini che NON sono ancora stati spediti e stampa la lista
ordini_non_spediti = df[df['Spedito'] == False][['Data', 'Cliente', 'Prodotto', 'Totale']]
print("\nOrdini non spediti:")
print(ordini_non_spediti)

# Calcola il fatturato totale per ogni cliente (somma dei Totali) e ordina la classifica decrescente.
fatturato_per_cliente = df.groupby('Cliente')['Totale'].sum().sort_values(ascending=False)
print("\nFatturato totale per ogni cliente (classifica decrescente):")
print(fatturato_per_cliente)

# Trova il prodotto più venduto in termini di quantità totale.
prodotto_piu_venduto = df.groupby('Prodotto')['Quantità'].sum().idxmax()
print("\nProdotto più venduto in termini di quantità totale:")
print(prodotto_piu_venduto)

# (Extra) Trova per ogni giorno il fatturato giornaliero (anche con un grafico a barre).
fatturato_giornaliero = df.groupby('Data')['Totale'].sum()
print("\nFatturato giornaliero:")
print(fatturato_giornaliero)

# Grafico a barre del fatturato giornaliero
# import matplotlib.pyplot as plt
# #plt.switch_backend('TkAgg')
# fatturato_giornaliero.plot(kind='bar', figsize=(10, 5))
# plt.title('Fatturato Giornaliero')
# plt.xlabel('Data')
# plt.ylabel('Fatturato Totale')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# (Extra) Calcola la media del prezzo unitario per ogni prodotto.
media_prezzo_per_prodotto = df.groupby('Prodotto')['Prezzo_unitario'].mean()
print("\nMedia del prezzo unitario per ogni prodotto:")
print(media_prezzo_per_prodotto)


