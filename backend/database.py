from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(
    database_url
)

def fetch_lap(id, lap, params = None):
    import pandas as pd
    query = """
    SELECT * 
    FROM telemetry_data_cota 
    WHERE normalized_id = %(id)s::TEXT
    AND lap = %(lap)s
    """
    return pd.read_sql_query(query, engine, params={"id": str(id), "lap": lap})