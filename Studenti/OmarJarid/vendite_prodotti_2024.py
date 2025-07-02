import pandas as pd
import matplotlib.pyplot as plt

# Crea il DataFrame.
dati = {
    "Mese": ["Gen", "Feb", "Mar", "Apr"] * 3,
    "Prodotto": ["A"] * 4 + ["B"] * 4 + ["C"] * 4,
    "Quantità": [
        120, 135, 150, 145,  # A
        90, 95, 100, 105,    # B
        60, 65, 70, 80,      # C
    ]
}

df = pd.DataFrame(dati)

# Esplora.
print(df.head(6))
print(df.dtypes)

# Filtri base.
prodotto_b = df[df["Prodotto"] == "B"]
oltre_100 = df[df["Quantità"] > 100]
mese_qta_prodotto_a = df.loc[df["Prodotto"] == "A", ["Mese", "Quantità"]]

print(prodotto_b)
print(oltre_100)
print(mese_qta_prodotto_a)

# Filtri extra.
prodotto_c_fino_70 = df[(df["Prodotto"] == "C") & (df["Quantità"] <= 70)]
print(prodotto_c_fino_70)

gennaio_febbraio = df[df["Mese"].isin(["Gen", "Feb"])]
print(gennaio_febbraio)

tra_90_e_130 = df[df["Quantità"].between(90, 130)]
print(tra_90_e_130)

senza_aprile = df[df["Mese"] != "Apr"]
print(senza_aprile)

# Aggregato semplice.
totali = df.groupby("Prodotto")["Quantità"].sum()
print(totali)

# Visualizzazione con 2 subplot.
fig, axes = plt.subplots(1, 2, figsize = (10, 4))

# Subplot 1 - Grafico a barre dei totali.
totali.plot(kind = "bar", ax = axes[0])
axes[0].set_title("Totale vendite per prodotto")
axes[0].set_ylabel("Unità vendute")

# Subplot 2 - Andamento mensile del prodotto B.
prod_b = df[df["Prodotto"] == "B"]
axes[1].plot(prod_b["Mese"], prod_b["Quantità"], marker = "o")
axes[1].set_title("Prodotto B – andamento gennaio-aprile")
axes[1].set_ylabel("Unità vendute")

# Pulizia secondo grafico.
axes[1].cla()

totale_mensile = df.groupby("Mese")["Quantità"].sum()

dataframe_filtro = df[
    ((df["Prodotto"] == "A") & (df["Quantità"] > 130)) | 
    ((df["Prodotto"] == "C") & (df["Quantità"] < 70))
]

axes[1].scatter(dataframe_filtro["Mese"], dataframe_filtro["Quantità"])

plt.tight_layout()
plt.show()