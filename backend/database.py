from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(
    database_url
)

def query(sql, params=None):
    import pandas as pd
    return pd.read_sql_query(sql, engine, params=params)

    
target_df, fastest_df = getTelemetry(15,3) 

print(target_df.head(), fastest_df.head())