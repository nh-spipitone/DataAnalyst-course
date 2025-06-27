import pandas as pd

df = pd.read_csv("DataAnalyst-course\Esercizi\Giorno 2\prova.csv")
print(df)
df["Totale"] = df["Prezzo_unitario"] * df["Quantità"]
print(df)