import csv
from datetime import datetime

def convertTime(time_str):
    if(time_str == ""):
        return -1.0

    time_object = datetime.strptime(time_str, '%M:%S.%f')

    total_seconds = time_object.minute * 60 + time_object.second + time_object.microsecond / 1_000_000.0
    return total_seconds

input_file =  input("Input desired file to read from: ")
output_file = input("Input desired file to write to: ")

with open(input_file, 'r', newline='' ) as infile:
    reader = csv.reader(infile, delimiter=";") 
    data = list(reader) 

newData = [["id", "lap1", "lap2", "lap3", "lap4", "lap5", "lap6", "lap7", "lap8", "lap9", "lap10"]] 

for i in range(1,len(data)):
    newData.append([])
    newData[i].append(data[i][0])
    for j in range(4, len(data[i]), 2):
        newData[i].append(convertTime(data[i][j]))

print(newData)

with open(output_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    csv_writer.writerow(newData[0])

    csv_writer.writerows(newData[1:])

print(f"Data successfully written to {output_file}")
