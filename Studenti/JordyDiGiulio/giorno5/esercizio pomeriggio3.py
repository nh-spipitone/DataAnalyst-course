import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np




# Esercizio 3: Analisi vendite mensili + Line plot
# Obiettivo: Visualizzare l’andamento delle vendite nel tempo.

# Istruzioni:

# Usa un dataset sales.csv con almeno due colonne: Data e Vendite.

# Assicurati che la colonna Data sia in formato datetime.

# Raggruppa le vendite per mese (usa resample("M") o estrai month).

# Crea un grafico a linee dell’andamento vendite.


df = pd.read_csv(r'Studenti\JordyDiGiulio\giorno5\sales.csv')


df['Data'] = pd.to_datetime(df['Data'])

df.set_index('Data', inplace=True)

vendite_mensili = df['Vendite'].resample('M').sum()

# andamento mensile delle vendite
plt.figure(figsize=(12,6))
plt.plot(vendite_mensili.index, vendite_mensili.values, marker='o')
plt.xlabel('Mese')
plt.ylabel('Vendite totali')
plt.title('Andamento vendite mensili')
plt.grid(True)
plt.tight_layout()
plt.show()


# percentuale vendite al mese
plt.figure(figsize=(8,6))
plt.pie(vendite_mensili, labels=vendite_mensili.index.strftime('%b'), autopct='%1.1f%%')
plt.tight_layout()
plt.show()