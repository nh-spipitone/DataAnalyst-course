import pandas as pd
from sklearn.impute import KNNImputer


df = pd.read_csv(r"Esercizi\Giorno 7\meteo.csv")
# Identificazione valori mancanti
mancanti = df.isna().sum()
print("Valori mancanti per colonna:\n", mancanti)


# Imputazione avanzata
imputer = KNNImputer(n_neighbors=5)  # Inizializza l'imputer KNN con 3 vicini
df_imputato = pd.DataFrame(
    imputer.fit_transform(df.select_dtypes(include=["float64", "int64"])),
    columns=df.select_dtypes(include=["float64", "int64"]).columns,
)
print("DataFrame dopo imputazione KNN:\n", df_imputato)


# Interpolazione per serie temporali
df["Temperatura_interp"] = df["Temperatura"].interpolate(method="cubic")
print(
    "Temperatura dopo interpolazione:\n",
    df[["Data", "Temperatura", "Temperatura_interp"]],
)


# df["Temperatura"] = df["Temperatura"].interpolate(method="cubic")
# print(
#     "Temperatura dopo interpolazione:\n",
#     df["Temperatura"],
# )
