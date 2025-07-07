import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5433/mydatabase"
)


with engine.begin() as conn:
    # ---------- DROP ---------------------------------------
    conn.execute(
        text(
            """
        DROP TABLE IF EXISTS studenti;  -- elimino tabella se esiste
    """
        )
    )
