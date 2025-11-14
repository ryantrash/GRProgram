class Vehicle:
    def __init__(self, id, telemetry):
        self.id = id 
        self.angle = [] 
        self.acc = [] 
        self.speed = [] 
        self.brake = [] 

        for index, row in telemetry.iterrows():
            tName = row['telemetry_name']
            tEntry = [row["telemetry_value"], row["meta_time"]] 
            if tName == "Steering_Angle":
                self.angle.append(tEntry)
            elif tName == "aps": 
                self.acc.append(tEntry)
            elif tName == "Speed":
                self.speed.append(tEntry)
            elif tName == "pbrake_f":
                self.brake.append(tEntry)