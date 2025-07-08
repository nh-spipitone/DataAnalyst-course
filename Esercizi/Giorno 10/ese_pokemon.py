import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5433/mydatabase"
)


def split_stats_columns(df):
    """
    Funzione che estrae le statistiche dalla colonna 'stats' e le aggiunge come colonne separate
    """
    # Estrarre tutte le statistiche usando regex con gruppi di cattura
    # r"hp=(\d+)" cerca "hp=" seguito da uno o più numeri, cattura solo i numeri
    df["hp"] = df["stats"].str.extract(r"hp=(\d+)").astype(int)
    df["attack"] = df["stats"].str.extract(r"attack=(\d+)").astype(int)
    df["defense"] = df["stats"].str.extract(r"defense=(\d+)").astype(int)
    # Per special-attack e special-defense usa il trattino nel regex
    df["special_attack"] = df["stats"].str.extract(r"special-attack=(\d+)").astype(int)
    df["special_defense"] = (
        df["stats"].str.extract(r"special-defense=(\d+)").astype(int)
    )
    df["speed"] = df["stats"].str.extract(r"speed=(\d+)").astype(int)

    return df


def search_pokemon_by_name(name, engine):
    """
    Funzione che cerca un Pokémon per nome nel database
    """
    name = name.lower()
    query = text(f"SELECT * FROM pokemon WHERE lower(name) = '{name}'")
    result = pd.read_sql(query, engine)
    return result


df = pd.read_csv(r"Esercizi\Giorno 10\pokemon_data.csv")
df = split_stats_columns(df)
print(df.head())

df.to_sql("pokemon", engine, if_exists="replace", index=False)

query = text("select name, types ,hp from pokemon where types LIKE '%fire%' AND hp >70")
pokemon_tipo_fuoco = pd.read_sql(query, engine)
print(pokemon_tipo_fuoco)
pokemon_tipo_fuoco.to_excel("pokemon_tipo_fuoco.xlsx", index=False)

pokemon_con_piu_attacco = pd.read_sql(
    "SELECT name,attack from pokemon ORDER by attack desc LIMIT 1",
    engine,
)
print("#######")
print(pokemon_con_piu_attacco)

print("#######" * 3)
Moltres = pd.read_sql("SELECT name, stats from pokemon where name='moltres'", engine)
print(Moltres)

while True:
    nome_pokemon = input(
        "Inserisci il nome del Pokémon da cercare (o 'exit' per uscire): "
    )
    if nome_pokemon.lower() == "exit":
        break
    pokemon = search_pokemon_by_name(nome_pokemon, engine)
    if not pokemon.empty:
        print(f"Dettagli del Pokémon '{nome_pokemon}':")
        print(pokemon)
    else:
        print(f"Nessun Pokémon trovato con il nome '{nome_pokemon}'.")
