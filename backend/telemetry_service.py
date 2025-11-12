from database import query, engine
from data_processing import getFastestLaps, load_laptimes
import pandas as pd 

def getTelemetryFor(target, lap):
    lap_df = load_laptimes("./COTA/race_1/laptimes.csv")
    fastest = getFastestLaps(lap_df) 

    query = "SELECT * FROM telemetry_data_cota WHERE normalized_id = %(id)s AND lap = %(lap)s"
    target_df = pd.read_sql_query(query, engine, params={"id": str(target), "lap": str(lap)}) 
    fastest_id = fastest[lap-1][0]
    fastest_df = pd.read_sql_query(query, engine, params={"id": str(fastest_id), "lap": str(lap)})

    return target_df, fastest_df

target_df, fastest_df = getTelemetryFor(13, 2)
print(target_df.head(), fastest_df.head())