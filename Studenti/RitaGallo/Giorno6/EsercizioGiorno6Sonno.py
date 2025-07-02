import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("Esercizi\Giorno 6\Health and Sleep relation 2024\Sleep_health_and_lifestyle_dataset.csv")

# print(df.head())
# print(df.info())

# 1. Tipi di dato
# Definiamo le colonne che dovrebbero essere numeriche
numeric_cols = ["Age", "Sleep Duration", "Physical Activity Level",
"Stress Level", "Heart Rate", "Daily Steps"]
# Convertiamo queste colonne in tipo numerico, sostituendo eventuali valori
# non convertibili con NaN (errors="coerce")
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

df["Sleep Disorder"] = df["Sleep Disorder"].fillna("None").astype(str)

bp_split =df["Blood Pressure"].str.split("/", expand = True)

df["Systolic"] = pd.to_numeric(bp_split[0])
df["Diastolic"] = pd.to_numeric(bp_split[1])


media_sonno = df.groupby("Gender")["Sleep Duration"].mean()
quantita_persone = df["Sleep Disorder"].value_counts().loc[["Sleep Apnea", "None"]]
# print(media_sonno)
# print(quantita_persone)

