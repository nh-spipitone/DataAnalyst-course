import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
)

df= pd.read_csv(r"Esercizi\Giorno 10\pokemon_data.csv")
print(df.head())

df.to_sql("pokemon",engine, if_exists="replace",index=False)
query="""select types from pokemon where types LIKE '%fire%'"""
pokemon_tipo_fuoco=pd.read_sql(str(query),engine)
print(pokemon_tipo_fuoco)



