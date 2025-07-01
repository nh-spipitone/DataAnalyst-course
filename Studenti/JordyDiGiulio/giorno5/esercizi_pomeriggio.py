import pandas as pd
import matplotlib.pyplot as plt 

# Esercizio 1: Analisi passeggeri Titanic + Istogramma dell'età
# Obiettivo: Analizzare e visualizzare la distribuzione dell’età dei passeggeri del Titanic.

# Istruzioni:

# Carica il dataset titanic.csv.

# Rimuovi le righe con età mancante (Age).

# Calcola:

# L’età media

# Il numero totale di passeggeri

# Crea un istogramma dell’età (Age) con matplotlib.pyplot.hist().

titanic = pd.read_csv(r'Studenti\JordyDiGiulio\giorno5\titanic.csv').dropna(subset=['Age'])

media_età = titanic['Age'].mean()
totale_passeggeri = titanic['Name'].count()


plt.figure(figsize=(10,5))
plt.hist(titanic['Age'], bins=10, align='mid', color='skyblue', edgecolor='black')
plt.tight_layout()
plt.show()



#Esercizio 2: Bar plot sopravvissuti per sesso
# Obiettivo: Confrontare il numero di sopravvissuti per genere.

# Istruzioni:

# Usa ancora titanic.csv.

# Raggruppa per Sex e Survived, poi conta quanti passeggeri ci sono per ogni gruppo.

# Trasforma i dati in un DataFrame adatto a un bar plot (es. pivot con unstack()).

# Visualizza i risultati con un grafico a barre (.plot(kind='bar')).



sopravvissuti_uomini = titanic[(titanic['Sex'] == 'male') & (titanic['Survived'] == 1)]['Name'].tolist()
sopravvissuti_donne = titanic[(titanic['Sex'] == 'female') & (titanic['Survived'] == 1)]['Name'].tolist()
totale_sopravvissuti = len(sopravvissuti_uomini)+len(sopravvissuti_donne)

plt.figure(figsize=(10,6))
plt.bar(['uomini sopravvissuti', 'donne sopravvissute'], [len(sopravvissuti_uomini), len(sopravvissuti_donne)], color=['green', 'orange'])
plt.xlabel('Sesso')
plt.ylabel('Numero di sopravvissuti')
plt.yticks(range(0, totale_sopravvissuti+1, 2))
plt.tight_layout()
plt.show()

