import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

'''
Esercizio: Creazione di un Report Completo sul Titanic
🎯 Obiettivo:
Creare un report completo che mostri:

Il numero di sopravvissuti per classe e sesso.

La tariffa media per ogni combinazione di classe e sesso.

Ordinare il report per classe e sesso.

Infine, visualizzare il numero di sopravvissuti per classe e sesso con un grafico a barre.

📋 Istruzioni per la consegna:
Carica il dataset Titanic:

Utilizza il file titanic.csv per caricare i dati dei passeggeri del Titanic.

Passo 1:

Utilizza pd.read_csv() per caricare il dataset.

Raggruppa i dati per classe e sesso:

Usa la funzione groupby() per raggruppare i dati per le colonne Pclass (classe del biglietto) e Sex (sesso).

Passo 2:

Raggruppa per le colonne Pclass e Sex e calcola:

Il numero di sopravvissuti (utilizzando sum() sulla colonna Survived).

La tariffa media (utilizzando mean() sulla colonna Fare).

Ordinamento dei risultati:

Ordina i risultati prima per classe (Pclass) e poi per sesso (Sex).

Usa sort_values() per fare l'ordinamento in ordine crescente.

Visualizza i risultati:

Crea un DataFrame con i risultati ottenuti.

Stampa i risultati per verificarne la correttezza.

Grafico a barre:

Crea un grafico a barre per visualizzare il numero di sopravvissuti per classe e sesso.

Utilizza matplotlib o seaborn per visualizzare il grafico.

Assicurati di etichettare correttamente gli assi e aggiungere un titolo al grafico.
'''


df = pd.read_csv(r'Studenti\JordyDiGiulio\Giorno 6\titanic-1.csv')

reports = df.groupby(['Pclass', 'Sex']).agg(
    Sopravvissuti=('Survived', 'sum'),
    Tariffa_media=('Fare', 'mean')
).reset_index()

reports = reports.sort_values(by=['Pclass', 'Sex'])


plt.figure(figsize=(8,6))

# prova con plt

for sex in ['male', 'female']:
    subset = reports[reports['Sex'] == sex]
    plt.bar(subset['Pclass'].astype(str), subset['Sopravvissuti'], label=sex)
    


# prova con sns

"""sns.barplot(
    data=reports,
    x='Pclass',
    y='Sopravvissuti',
    hue='Sex',
    palette='pastel'
)
"""

plt.title('Sopravvissuti per classe e sesso')
plt.xlabel('Classe')
plt.ylabel('Numero sopravvissuti')
plt.legend(title='Sesso')
plt.tight_layout()
plt.show()


