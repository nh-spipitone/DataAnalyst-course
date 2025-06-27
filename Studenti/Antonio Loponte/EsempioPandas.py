import pandas as pd
import os

print("Directory corrente:", os.getcwd())

csv_path = r'C:\Users\lopon\OneDrive\Desktop\corso DataAnalyst\DataAnalyst-course\Studenti\Antonio Loponte\viaggi.csv'

try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    print(f"File 'viaggi.csv' non trovato nel percorso: {csv_path}")
    exit()

print(df)


print("Aggiungi un nuovo viaggio:")
nuova_riga = {}
for col in df.columns:
    valore = input(f"Inserisci valore per '{col}': ")
    nuova_riga[col] = valore

df = pd.concat([df, pd.DataFrame([nuova_riga])], ignore_index=True)

print("Dati aggiornati:")
print(df)


df.to_csv(r'C:\Users\lopon\OneDrive\Desktop\corso DataAnalyst\DataAnalyst-course\Studenti\Antonio Loponte\dati_modificati.csv', index=False)

