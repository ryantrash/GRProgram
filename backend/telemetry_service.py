from backend.database import fetch_lap
from backend.data_processing import getFastestLaps, load_laptimes
from backend.vehicle import Vehicle
import pandas as pd


class TelemetryService:
    def __init__(self, laptime_path="./COTA/race_1/laptimes.csv"):
        self.lap_df = load_laptimes(laptime_path)
        self.fastest = getFastestLaps(self.lap_df)

        self.cache = {}

    def get_vehicle(self, driver_id, lap):
        key = (driver_id, lap)

        if key in self.cache:
            return self.cache[key]

        df = fetch_lap(driver_id, lap)
        v = Vehicle(driver_id, df)

        self.cache[key] = v
        return v

    def get_fastest_vehicle(self, lap):
        fastest_id, _ = self.fastest[lap]
        return self.get_vehicle(fastest_id, lap)

    def compare(self, driver_id, lap):
        v_target = self.get_vehicle(driver_id, lap)
        v_fastest = self.get_fastest_vehicle(lap)

        acc_delta = {}
        
        target_iter = iter(v_target.acc.values())
        fastest_iter = iter(v_fastest.acc.values())
        try: 
            for i in range(1, len(v_target.acc)):
                target_val = next(target_iter)
                fastest_val = next(fastest_iter)

                acc_delta[i] = target_val - fastest_val
        except: 
            print("limit reached")
        return acc_delta


test = TelemetryService()

print(test.compare(3, 3))
