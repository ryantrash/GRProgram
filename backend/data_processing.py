import pandas as pd

def load_laptimes(path):
    return pd.read_csv(path)

def getFastestLaps(df):
    laps = []
    for colname in df.columns[1:]:
        valid_times = df[colname][df[colname] > 0]
        if not valid_times.empty:
            fastest_time = valid_times.min()
            car_id = valid_times.idxmin()
            laps.append((car_id, fastest_time))
    return laps
