import pandas as pd
import numpy as np
import random
import math
import sys

#download CSV of US cities here: https://github.com/kelvins/US-Cities-Database/blob/main/csv/us_cities.csv
towns = pd.read_csv('us_cities.csv')

#take in user coords
def getUserCoords():
    try:
        user_coords = input("Please enter your coordinates (with several digits of precision) and desired search radius in the format 'lat, long, radius (mi)': ")
        user_coords = user_coords.split(',')
        lat = float(user_coords[0])
        long = float(user_coords[1])
        radius = float(user_coords[2])
        return lat, long, radius
    except:
        print("Invalid input. Please enter your coordinates in the format 'lat, long, radius (mi)': ")
        sys.exit()

coords = getUserCoords()
inputLat = coords[0]
inputLong = coords[1]
inputRadius = coords[2]

#calculate haversine distance between all towns in CSV and user input
townsLat = towns['LATITUDE']
townsLong = towns['LONGITUDE']
towns['LAT_rad'], towns['LON_rad'] = np.radians(towns['LATITUDE']), np.radians(towns['LONGITUDE'])
towns['dLON'] = towns['LON_rad'] - math.radians(inputLong)
towns['dLAT'] = towns['LAT_rad'] - math.radians(inputLat)
towns['distance'] = 6367 * 2 * np.arcsin(np.sqrt(np.sin(towns['dLAT']/2)**2 + math.cos(math.radians(inputLat)) * np.cos(towns['LAT_rad']) * np.sin(towns['dLON']/2)**2))

#filter out towns outside of radius
inputRadius = inputRadius/0.621371
towns = towns[towns['distance'] <= inputRadius]

#return random town within radius
randomTown = towns.sample()
state = randomTown['STATE_NAME']
city = randomTown['CITY']
print(city.iloc[0] + ', ' + state.iloc[0])














