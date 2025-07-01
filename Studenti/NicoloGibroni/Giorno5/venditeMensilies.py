# Esercizio 3: Analisi vendite mensili + Line plot
# Obiettivo: Visualizzare l’andamento delle vendite nel tempo.
# Istruzioni:
# Usa un dataset sales.csv con almeno due colonne: Data e Vendite.
# Assicurati che la colonna Data sia in formato datetime.
# Raggruppa le vendite per mese (usa resample("M") o estrai month).
# Crea un grafico a linee dell’andamento vendite.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'DataAnalyst-course\Studenti\NicoloGibroni\Giorno5\sales.csv')

df["Data"] = pd.to_datetime(df['Data'])
df["Mese"] = df['Data'].dt.to_period("M")
data = df.groupby("Mese")["Vendite"].sum().reset_index()
data.plot()
plt.xlabel("Data")
plt.ylabel("Vendite")
plt.show()

# Calcolare l’ammontare totale delle vendite e visualizzare ciascun 
# mese come percentuale del totale in un grafico a torta (pie chart).

plt.pie(data["Vendite"],labels=data["Mese"].astype(str),autopct="%1.1f%%")
plt.tight_layout()
plt.show()

# Trovare e visualizzare i 3 giorni con le vendite più alte, 
# in ordine decrescente e crea un grafico a barre verticali per confrontare le vendite di quei 3 giorni.

df["Giorno"] = df['Data'].dt.to_period("D")
data2 = df.groupby("Giorno")["Vendite"].sum().sort_values(ascending=False).head(3)
data2.plot.bar()
plt.xlabel("Data")
plt.ylabel("Vendite")
plt.show()
