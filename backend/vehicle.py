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
                
        self.angle = self.toSeconds(self.angle)
    
    def toSeconds(self, arr): 
        by_seconds = {}
        count = 1
        vals = [arr[0][0]]
        current_second = arr[0][1][14:18]
        
        for i in range(1, len(arr)):
            val = arr[i][1]
            if current_second == val[14:18]: 
                vals.append(arr[i][0])
            else: 
                cur = arr[i][1] 
                by_seconds[i] = (round(sum(vals)/len(vals), 5))
                vals = [arr[i][0]] 
    
        by_seconds[len(by_seconds)] = (round(sum(vals)/len(vals), 5))
        return by_seconds  