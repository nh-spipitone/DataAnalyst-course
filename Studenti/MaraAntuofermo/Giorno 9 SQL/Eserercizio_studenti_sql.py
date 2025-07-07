import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase")

