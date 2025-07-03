import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


'''
Esercizio: Analisi delle app per categoria e numero di download
🎯 Obiettivo:
Il tuo obiettivo è analizzare il numero di download per categoria di app, e calcolare la media delle valutazioni per ciascuna categoria. Successivamente, crea un grafico a barre per visualizzare i download totali per categoria.

📋 Istruzioni per la consegna:
Carica il dataset:

Usa il file googleplaystore.csv per caricare i dati che contengono informazioni sulle app disponibili su Google Play Store.

Prepara i dati:

Pulisci la colonna Installs per rimuovere simboli non numerici (+ e ,), assicurandoti che i valori siano numerici.

Converte la colonna Installs in formato numerico (tipicamente interi).

Rimuovi le righe con valori mancanti nella colonna Rating e Installs.

Raggruppa i dati per categoria:

Raggruppa i dati per categoria (Category) e calcola:

Il totale dei download per ciascuna categoria (somma della colonna Installs).

La media delle valutazioni (colonna Rating) per ciascuna categoria.

Filtra i dati:

Considera solo le categorie che hanno almeno 10 app.

Visualizza i risultati:

Crea un grafico a barre che mostri la somma totale dei download per categoria, ordinato in ordine decrescente.

Aggiungi etichette chiare sugli assi e un titolo per il grafico.
'''


df = pd.read_csv(r'Studenti\JordyDiGiulio\Giorno 6\googleplaystore.csv')

# installs_list = df['Installs'].to_list()

# installs_list = [x.replace(',', '').replace('+', '') for x in installs_list]

# df['Installs'] = installs_list

# df[['Installs', 'Rating']].dropna()

# df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

# df_ordinata = df.groupby('Category').agg(
#     totale_downloads=('Installs', 'sum'),
#     media_rating =('Rating', 'mean')
# ).reset_index()

# df_finale = df_ordinata.sort_values(by='totale_downloads', ascending=False)

# print(df_ordinata)

# plt.figure(figsize=(8,6))
# sns.barplot(
#     data=df_finale,
#     x='Category',
#     y='totale_downloads',
#     palette='pastel'
# )

# plt.title('Somma totale download per categoria')
# plt.xlabel('Categoria')
# plt.ylabel('Downloads')
# plt.legend()
# plt.tight_layout()
# plt.show()


'''Esercizio 2: Top 5 App con il Maggior Numero di Recensioni
🎯 Obiettivo:
Identificare le 5 app con il maggior numero di recensioni e visualizzare i risultati.

📋 Istruzioni per la consegna:

Carica il dataset: Usa il file googleplaystore.csv per caricare i dati.

Rimuovi i valori non numerici dalla colonna Reviews (eventuali valori che non sono numeri).

Filtra:

Ordina il dataset in base al numero di recensioni (Reviews) in ordine decrescente.

Seleziona le prime 5 app con il maggior numero di recensioni.

Visualizzazione:

Crea un grafico a barre per visualizzare le prime 5 app con il maggiore numero di recensioni.
'''

medie = df.groupby('Category')['Reviews'].mean().reset_index()
df_review = df.groupby('App')['Reviews'].sum().reset_index().sort_values(by='Reviews', ascending=False)
print(medie)
print(df_review)



plt.figure(figsize=(8,6))
sns.barplot(
    data=df_review,
    x='App',
    y='Reviews',
    palette='pastel'
)

plt.title('Somma totale download per categoria')
plt.xlabel('App')
plt.ylabel('Reviews')
plt.legend()
plt.tight_layout()
plt.show()




