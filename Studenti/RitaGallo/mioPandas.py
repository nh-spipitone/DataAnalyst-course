import pandas as pd

df = pd.read_csv("Esercizii\Giorno 2\prova.csv")
print(df)

df["Totale"] = df["Prezzo Unitario"] * df["Quantita"]
print(df)
