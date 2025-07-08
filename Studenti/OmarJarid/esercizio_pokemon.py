import pandas as pd
from datetime import date
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
)

def split_stats_columns(df):
    df["hp"] = df["stats"].str.extract(r"hp=(\d+)").astype(int)
    df["attack"] = df["stats"].str.extract(r"attack=(\d+)").astype(int)
    df["defense"] = df["stats"].str.extract(r"defense=(\d+)").astype(int)
    df["speed"] = df["stats"].str.extract(r"speed=(\d+)").astype(int)
    df["special_attack"] = df["stats"].str.extract(r"special-attack=(\d+)").astype(int)
    df["special_defense"] = df["stats"].str.extract(r"special-defense=(\d+)").astype(int)
    return df

def search_pokemon_by_name(name):
    query = text(f"""
    SELECT *
    FROM   pokemon
    WHERE  name = '{name.lower()}'
    """)
    return pd.read_sql(query, engine)

df = pd.read_csv(r"Esercizi\Giorno 10\pokemon_data.csv")
df = split_stats_columns(df)
df.to_sql("pokemon", engine, if_exists = "replace", index = False)

query = text("""
SELECT *
FROM   pokemon
WHERE  types LIKE '%fire%' AND hp > 70
""")
pokemon_tipo_fuoco = pd.read_sql(query, engine)
print(pokemon_tipo_fuoco)
pokemon_tipo_fuoco.to_excel("pokemon_tipo_fuoco.xlsx", index = False)

# Mostra il Pokémon con l'attacco più alto di tutti
query = text("""
SELECT   name, attack
FROM     pokemon
ORDER BY attack DESC
LIMIT    1
""")
pokemon_attacco_piu_alto = pd.read_sql(query, engine)
print(pokemon_attacco_piu_alto)

# Mostra le statistiche di Moltres
query = text("""
SELECT name, stats
FROM   pokemon
WHERE  name = 'moltres'
""")
pokemon_statistiche_moltres = pd.read_sql(query, engine)
print(pokemon_statistiche_moltres)

while True:
    nome_pokemon = input("Inserisci il nome del Pokémon da cercare (o 'exit' per uscire): ")
    if nome_pokemon.lower() == 'exit':break
    pokemon = search_pokemon_by_name(nome_pokemon)
    if not pokemon.empty:
        print(pokemon)
    else:
        print(f"Nessun Pokémon trovato con il nome '{nome_pokemon}'.")

query = text("""
    SELECT 
             name, 
             hp, 
             attack,
             defense,
             speed,
             special_attack,
             special_defense,
             (hp + attack + defense + speed + special_attack + special_defense)/6 AS avg_stats
    FROM     pokemon
    ORDER BY avg_stats DESC
    LIMIT    5
""")
pokemon_statistiche_max = pd.read_sql(query, engine)
print(pokemon_statistiche_max)