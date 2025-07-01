import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("DataAnalyst-course\Esercizi\Giorno 5\ordini_amazon.csv")
# print(df.head())

ordini_consegnati = []

df_consegnati = df[df['Stato'] == 'Consegnato']
print(df_consegnati)

df["Totale"] = df["Quantità"] * df["Prezzo"]

totale_per_categoria = df.goupby("Categoria") ["Totale"].sum()
print(totale_per_categoria)

plt.figure(figsize=(10, 8))
totale_per_categoria = df.groubpy("Categoria") ["Totale"].sum()
totale_per_categoria.plot(kind = "bar", color = "turquoise")
plt.title("Totale spero per categoria", fontsize = 16)
plt.xlabel8("Categoria", fontsize = 14)
plt.ylabel("Totale", fontsize = 14)
plt.tight_layout()
plt.show()

df["Data"] = pd.to_datetime(df["Data"])

df["Mese"] = df["Data"].dt.to_period("M")
spesa_mensile = df.groupby("Mese") ["Totale"].sum()

plt.figure(figsize = (8, 4))
spesa_mensile.plot(marker = "o", linestyle ="-", color = "orange")
plt.title("Spesa mensile", fontsize = 16)
plt.xlabel("Data", fontsize = 14)
plt.ylabel("Spesa", fontsize = 14)
plt.tight_layout()
plt.show()

mese_piu_costoso = spesa_mensile.idmax()
print(f"Mese più costoso {mese_piu_costoso}")
categoria_piu_costosa = totale_per_categoria.idmax()
categoria_piu_costosa_tot = totale_per_categoria.max()
print(f"La cetegoria più costosa è {categoria_piu_costosa} con un totale di {categoria_piu_costosa_tot}")

