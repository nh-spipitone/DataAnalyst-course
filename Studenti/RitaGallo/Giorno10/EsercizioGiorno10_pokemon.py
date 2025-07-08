import pandas as pd

from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
)

def split_stats_columns(df):
    df["hp"] = df["stats"].str.extract(r"hp=(\d+)").astype(int)
    df["attack"] = df["stats"].str.extract(r"attack=(\d+)").astype(int)
    df["defense"] = df["stats"].str.extract(r"defense=(\d+)").astype(int)
    df["special_attack"] = df["stats"].str.extract(r"special-attack=(\d+)").astype(int)
    df["special_defense"] = df["stats"].str.extract(r"special-defense=(\d+)").astype(int)
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


df = pd.read_csv("DataAnalyst-course//Esercizi//Giorno 10//pokemon_data.csv")
df = split_stats_columns(df)
print(df.head())

df.to_sql("pokemon", engine, if_exists="replace", index=False)

query = text("select name, types ,hp from pokemon where types LIKE '%fire%' AND hp >70")
pokemon_tipo_fuoco = pd.read_sql(query, engine)
print(pokemon_tipo_fuoco)
pokemon_tipo_fuoco.to_excel("pokemon_tipo_fuoco.xlsx", index=False)

pokemon_con_piu_attacco = pd.read_sql(
    "SELECT * FROM pokemon ORDER BY attack DESC LIMIT 1",
    engine,
)
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

top_5_pokemon_piu_forti = pd.read_sql(
    "SELECT name, hp, attack, defense, special_attack, special_defense, speed, (hp + attack + defense + special_attack + special_defense + speed)/6 AS avg_stats FROM pokemon ORDER BY avg_stats DESC LIMIT 5",
    engine,
) 
print("Top 5 Pokémon più forti:")
print(top_5_pokemon_piu_forti)  


