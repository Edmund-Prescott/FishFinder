# Data Source
# https://wdfw.wa.gov/fishing/locations/high-lakes?name=&county%5B0%5D=42&species=&page=0
import csv

# Read data from the text file
with open("WA_high_lakes.txt", "r") as file:
    data = file.readlines()

# Process the data and write it to a CSV file
with open("WA_high_lakes.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Acres", "Elevation", "County", "Latitude", "Longitude"])
    for line in data:
        fields = line.strip().split("\t")
        name = fields[0]
        acres = fields[1]
        elevation = fields[2]
        county = fields[3]
        latitude, longitude = fields[4].split(", ")
        writer.writerow([name, acres, elevation, county, latitude, longitude])

print("CSV file 'output.csv' has been created.")
