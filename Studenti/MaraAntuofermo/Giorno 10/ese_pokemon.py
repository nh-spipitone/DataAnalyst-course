import pandas as pd  # Importa la libreria pandas per la manipolazione dei dati
from sqlalchemy import (
    create_engine,
    text,
)  # Importa funzioni per collegarsi a un database SQL

engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
)  # Crea una connessione al database PostgreSQL


def split_stats_columns(df):
    """
    Funzione che estrae le statistiche dalla colonna 'stats' e le aggiunge come colonne separate
    """
    # Estrae il valore di 'hp' dalla colonna 'stats' usando regex e lo converte in intero
    df["hp"] = df["stats"].str.extract(r"hp=(\d+)").astype(int)
    # Estrae il valore di 'attack'
    df["attack"] = df["stats"].str.extract(r"attack=(\d+)").astype(int)
    # Estrae il valore di 'defense'
    df["defense"] = df["stats"].str.extract(r"defense=(\d+)").astype(int)
    # Estrae il valore di 'special-attack'
    df["special_attack"] = df["stats"].str.extract(r"special-attack=(\d+)").astype(int)
    # Estrae il valore di 'special-defense'
    df["special_defense"] = (
        df["stats"].str.extract(r"special-defense=(\d+)").astype(int)
    )
    # Estrae il valore di 'speed'
    df["speed"] = df["stats"].str.extract(r"speed=(\d+)").astype(int)

    return df  # Restituisce il DataFrame modificato


def search_pokemon_by_name(name, engine):
    """
    Funzione che cerca un Pokémon per nome nel database
    """
    name = name.lower()  # Converte il nome in minuscolo
    query = text(
        f"SELECT * FROM pokemon WHERE lower(name) = '{name}'"
    )  # Query SQL per cercare il Pokémon
    result = pd.read_sql(
        query, engine
    )  # Esegue la query e restituisce il risultato come DataFrame
    return result


df = pd.read_csv(
    r"DataAnalyst-course/Studenti/MaraAntuofermo/Giorno 10/pokemon_data.csv"
)  # Legge il file CSV con i dati dei Pokémon
df = split_stats_columns(
    df
)  # Applica la funzione per separare le statistiche in colonne
print(df.head())  # Stampa le prime 5 righe del DataFrame

df.to_sql(
    "pokemon", engine, if_exists="replace", index=False
)  # Salva il DataFrame nella tabella 'pokemon' del database

query = text("select name, types ,hp from pokemon where types LIKE '%fire%' AND hp >70")
# Query per selezionare i Pokémon di tipo fuoco con hp > 70
pokemon_tipo_fuoco = pd.read_sql(query, engine)  # Esegue la query e salva il risultato
print(pokemon_tipo_fuoco)  # Stampa i Pokémon trovati
pokemon_tipo_fuoco.to_excel(
    "pokemon_tipo_fuoco.xlsx", index=False
)  # Esporta il risultato in un file Excel

pokemon_con_piu_attacco = pd.read_sql(
    "SELECT name,attack from pokemon ORDER by attack desc LIMIT 1",
    engine,
)  # Query per trovare il Pokémon con più attacco
print("#######")
print(pokemon_con_piu_attacco)  # Stampa il Pokémon con più attacco

print("#######" * 3)
Moltres = pd.read_sql("SELECT name, stats from pokemon where name='moltres'", engine)
# Query per selezionare Moltres e le sue statistiche
print(Moltres)  # Stampa il risultato

while True:
    nome_pokemon = input(
        "Inserisci il nome del Pokémon da cercare (o 'exit' per uscire): "
    )  # Chiede all'utente il nome del Pokémon da cercare
    if nome_pokemon.lower() == "exit":  # Se l'utente scrive 'exit', esce dal ciclo
        break
    pokemon = search_pokemon_by_name(
        nome_pokemon, engine
    )  # Cerca il Pokémon nel database
    if not pokemon.empty:  # Se il Pokémon esiste
        print(f"Dettagli del Pokémon '{nome_pokemon}':")
        print(pokemon)  # Stampa i dettagli
    else:
        print(
            f"Nessun Pokémon trovato con il nome '{nome_pokemon}'."
        )  # Messaggio se non trovato

top_5_pokemon_piu_forti = pd.read_sql(
    "SELECT name, hp, attack, defense, special_attack, special_defense, speed, (hp + attack + defense + special_attack + special_defense + speed)/6 AS avg_stats FROM pokemon ORDER BY avg_stats DESC LIMIT 5",
    engine,
)  # Query per trovare i 5 Pokémon con la media statistiche più alta
print("Top 5 Pokémon più forti:")
print(top_5_pokemon_piu_forti)  # Stampa i 5 Pokémon più forti
