import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"DataAnalyst-course\Studenti\NicoloGibroni\Giorno7\sales_sample.csv")
per_categoria = df.groupby("Category")[["Sales", "Revenue"]].sum().reset_index()

# Esercizio 1: Analisi delle Vendite per Categoria
per_categoria.plot(kind="bar")
plt.xlabel("Categories")
plt.ylabel("Values in milioni")
plt.tight_layout()
plt.show()

# Esercizio 2: Analisi delle Vendite Mensili
df["Date"] = pd.to_datetime(df['Date'])
per_mese = df
per_mese["Date"] = per_mese['Date'].dt.to_period("M").sort_values(ascending=True)
per_mese_group = per_mese.groupby("Date")[["Sales", "Revenue"]].sum().reset_index()
per_mese_group.plot(marker="o")
plt.tight_layout()
plt.show()

# Esercizio 3: Top 5 Prodotti per Ricavi
df[["Sales", "Revenue"]] = df[["Sales", "Revenue"]].dropna()
df = df.sort_values("Revenue", ascending=False)
df.head(5).plot(kind="bar")
plt.tight_layout()
plt.show()

#-------------Questo è sbagliato
# Esercizio 1: Analisi delle Categorie con il Maggiore Incremento di Vendite Mensili
# 🎯 Obiettivo: Identificare le categorie con il maggior incremento nelle vendite mensili e visualizzare i risultati.
# Estrai il mese e l'anno dalla colonna Date per ottenere i dati su base mensile.
per_mese_sales = per_mese.groupby(["Category", "Date"])["Sales"].sum().reset_index()
per_mese_sales = per_mese.groupby(["Category", "Date"])["Sales"].diff().reset_index()
plt.plot(per_mese_sales["Date"],per_mese_sales["Sales"],marker="o")
plt.tight_layout()
plt.show()

# Identifica la categoria con il maggior incremento di vendite rispetto al mese precedente.
# Visualizza i risultati:
# Crea un grafico a linee che mostra l'andamento dell'incremento di vendite per la categoria con il maggior incremento mensile.