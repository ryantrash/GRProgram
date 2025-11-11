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
    for i in range(1, len(df.columns)):
        lap = df.columns[i] 
        coldata = df.iloc[:, i] 
        coldata.sort_values()
        fastest = -1.0
        for j in range(0, len(coldata)):
            time = coldata.iloc[j].item()
            car_id = coldata.index[i].item()
            if time > 0.0:
                laps.append([lap, car_id, time])
                break 
    return laps

lap_df = pd.read_csv("./COTA/race_1/laptimes.csv")
fastestLaps = getFastestLaps(lap_df) 
print(fastestLaps)