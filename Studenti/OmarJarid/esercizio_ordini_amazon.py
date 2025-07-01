import pandas as pd
import matplotlib.pyplot as plt

# Carica i dati.
df = pd.read_csv("Esercizi\\Giorno 5\\ordini_amazon.csv")
# print(df.head()) # Stampa solo le prime 5 righe.

# Filtra solo gli ordini con stato "Consegnato".
# Filtro creando un nuovo DataFrame a partire dal DataFrame originale.
df_consegnati = df[df['Stato'] == 'Consegnato']
#print(df_consegnati)

# Aggiungi una colonna "Totale" (Prezzo * Quantità)
df["Totale"] = df["Quantità"] * df["Prezzo"]

# Calcola il totale speso per categoria.
totale_per_categoria = df.groupby("Categoria")["Totale"].sum().reset_index()
print(totale_per_categoria)

# Crea un grafico a barre delle spese totali per categoria.
plt.figure(figsize = (10, 8))
totale_per_categoria = df.groupby("Categoria")["Totale"].sum()
totale_per_categoria.plot(kind = "bar", color = "turquoise")
plt.title("Totale speso per categoria", fontsize = 16)
plt.xlabel("Categoria", fontsize = 14)
plt.ylabel("Totale speso (€)", fontsize = 14)
plt.tight_layout()
plt.show()

# Visualizza l’andamento mensile della spesa totale (grafico a linee).
plt.figure(figsize = (8, 4))
totale_per_categoria.plot(marker = "o", linestyle = "--", color = "orange")
plt.title("Totale speso per categoria (linea)", fontsize = 16)
plt.xlabel("Categoria", fontsize = 14)
plt.ylabel("Totale speso (€)", fontsize = 14)
plt.show()

df["Data"] = pd.to_datetime(df["Data"])
df["Mese"] = df["Data"].dt.to_period("M")
spesa_mensile = df.groupby("Mese")["Totale"].sum()

plt.figure(figsize = (8, 4))
spesa_mensile.plot(marker = "o", linestyle = "-", color = "orange")
plt.title("Spesa mensile", fontsize = 16)
plt.xlabel("Data", fontsize = 14)
plt.ylabel("Spesa (€)", fontsize = 14)
plt.show()

mese_piu_costoso = spesa_mensile.idxmax()
print(f"Mese più costoso: {mese_piu_costoso}")

categoria_piu_costosa = totale_per_categoria.idxmax()
categoria_piu_costosa_tot = totale_per_categoria.max()
print(f"Categoria più costosa: {categoria_piu_costosa} con un totale di {categoria_piu_costosa_tot}€")