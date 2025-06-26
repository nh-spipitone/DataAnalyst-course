import pandas as pd

df = pd.read_csv("Esercizi\Girno2\prova.csv")
print(df)

df["Totale"] = df["Prezzo_unitario"] * df["Quantità"]
print(df)

ricavo_totale = df["Totale"].sum()
print(len(df["Prezzo_unitario"]))
media_prezzo = ricavo_totale / len(df["Prezzo_unitario"])

print(f"La media del prezzo unitario è: {media_prezzo} euro")
print(f"Il ricavo totale è: {ricavo_totale} euro")
