from sqlalchemy import create_engine
import pandas as pd 
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(
    database_url
)

def getFastestLaps(df):
    laps = []
    for colname in df.columns[1:]:
        valid_times = df[colname][df[colname] > 0]
        if not valid_times.empty:
            fastest_time = valid_times.min()
            car_id = valid_times.idxmin()
            laps.append((car_id, fastest_time))
    return laps


def getTelemetry(target, lap):
    lap_df = pd.read_csv("./COTA/race_1/laptimes.csv")
    fastest = getFastestLaps(lap_df) 

    query = "SELECT * FROM telemetry_data_cota WHERE normalized_id = %(id)s AND lap = %(lap)s"
    target_df = pd.read_sql_query(query, engine, params={"id": str(target), "lap": str(lap)}) 
    fastest_id = fastest[lap-1][0]
    fastest_df = pd.read_sql_query(query, engine, params={"id": str(fastest_id), "lap": str(lap)})

    return target_df, fastest_df
    
target_df, fastest_df = getTelemetry(15,3) 

print(target_df.head(), fastest_df.head())