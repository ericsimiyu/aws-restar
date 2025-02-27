import csv
import copy

# Defining a dictionary
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Iterate over initial keys and values of the dictionary
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

# Defining an empty list
myInventoryList = []

# Read from the CSV file
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = int(row[3])  # Convert to integer
            currentVehicle["range"] = int(row[4])  # Convert to integer
            currentVehicle["topSpeed"] = int(row[5])  # Convert to integer
            currentVehicle["zeroSixty"] = float(row[6])  # Convert to float
            currentVehicle["mileage"] = int(row[7])  # Convert to integer
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')

# Printing car inventory
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
    print("-----")