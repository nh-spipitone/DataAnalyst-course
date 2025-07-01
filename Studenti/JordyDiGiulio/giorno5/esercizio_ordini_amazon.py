import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Esercizi\\Giorno 5\\ordini_amazon.csv")
df_consegnati = df[df["Stato"] == "Consegnato"]
df["Totale"] = df["Quantità"] * df["Prezzo"]

totale_per_categoria = df.groupby("Categoria")["Totale"].sum()
print(totale_per_categoria)

plt.figure(figsize=(10, 8))
totale_per_categoria.plot(kind="bar", color="turquoise")
plt.title("Totale speso per categoria", fontsize=16)
plt.xlabel("Categoria", fontsize=14)
plt.ylabel("Totale speso (€)", fontsize=14)
plt.tight_layout()
plt.show()

df["Data"] = pd.to_datetime(df["Data"])
df["Mese"] = df["Data"].dt.to_period("M")
spesa_mensile = df.groupby("Mese")["Totale"].sum()

plt.figure(figsize=(8, 4))
spesa_mensile.plot(marker="o", linestyle="-", color="orange")
plt.title("Spesa mensile", fontsize=16)
plt.xlabel("Data", fontsize=14)
plt.ylabel("Spesa", fontsize=14)
plt.show()

mese_più_costoso = spesa_mensile.idxmax()
print(f"Mese più costoso: {mese_più_costoso}")

categoria_più_costosa = totale_per_categoria.idxmax()
categoria_più_costosa_tot = totale_per_categoria.max()
print(f"La categoria più costosa è {categoria_più_costosa} con un totale di {categoria_più_costosa_tot} €")
