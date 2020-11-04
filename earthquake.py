import requests
import json

if __name__ == "__main__":
     quakes= requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
                      params={
                          'starttime': "2000-01-01",
                          "maxlatitude": "58.723",
                          "minlatitude": "50.008",
                          "maxlongitude": "1.67",
                          "minlongitude": "-9.756",
                          "minmagnitude": "1",
                          "endtime": "2018-10-11",
                          "orderby": "time-asc"}
                      )

quakes_data = json.loads(quakes.text)
max_magnitudes = 0
coords = []

for quake in quakes_data['features']:
    if quake['properties']['mag'] > max_magnitudes:
        max_magnitude = quake['properties']['mag']
        coords = [quake['geometry']['coordinates']]
    elif quake['properties']['mag'] == max_magnitude:
        coords.append(quake['geometry']['coordinates'])

print("The maximum magnitude is {max_magnitude} "f"and it occured at coordinates {coords}.")






