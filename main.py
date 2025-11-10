from sqlalchemy import create_engine
import pandas as pd 
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(
    
)

def getFastestLaps(df):
    laps = {}
    for colname, coldata in df.items(): 
        laps[colname] = coldata.min().item()
    return laps

lap_df = pd.read_csv("./COTA/race_1/laptimes.csv")
fastestLaps = getFastestLaps(lap_df) 
print(fastestLaps)