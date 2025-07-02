import pandas as pd
import matplotlib.pyplot as plt

dati = {
    "Mese": ["Gen", "Feb", "Mar", "Apr"] * 3,
    "Prodotto": ["A"]*4 + ["B"]*4 + ["C"]*4,
    "Quantità": [120, 135, 150, 145,   # A
                 90,  95,  100, 105,    # B
                 60,  65,   70,  80]    # C
}
df = pd.DataFrame(dati)

df.head(6)
df.dtypes
print(df)

print(df[df["Prodotto"] == "B"])

print(df[df["Quantità"] > 100])

print(df.loc[df["Prodotto"] == "A", ["Mese", "Quantità"]])

print(df[(df["Prodotto"] == "C") & (df["Quantità"] <= 70)])

print(df[df["Mese"].isin(["Gen", "Feb"])])

print(df[df["Quantità"].between(90,130)])

print(df[df["Mese"] != "Apr"])

totali = df.groupby("Prodotto")["Quantità"].sum()
print(totali)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

totali.plot(kind="bar", ax=axes[0])
axes[0].set_title("Totale vendite per prodotto")
axes[0].set_ylabel("Unità vendute")

prod_b = df[df["Prodotto"] == "B"]
axes[1].plot(prod_b["Mese"], prod_b["Quantità"], marker="o")
axes[1].set_title("Prodotto B - andamento gennaio-aprile")
axes[1].set_ylabel("Unità vendute")
axes[1].cla()

totale_mensile = df.groupby("Mese")["Quantità"].sum()
dataframe_filtro = df[((df["Prodotto"] == "A") & (df["Quantità"] > 130)) | ((df["Prodotto"] == "C") & (df["Quantità"] < 70))]

axes[1].scatter(dataframe_filtro["Mese"], dataframe_filtro["Quantità"])

plt.tight_layout()
plt.show()
