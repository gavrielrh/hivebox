from fastapi import FastAPI
import requests
from datetime import datetime

app = FastAPI()

VERSION = "v0.0.1"

@app.get("/version")
def version():
    return VERSION

@app.get("/temperature")
def temperature():
    phenomenon = "temperature"
    date = datetime.now().isoformat() + 'Z'
    res = requests.get(f"https://api.opensensemap.org/boxes?date={date}&phenomenon={phenomenon}")
    all_boxes = res.json()
    c_count = 0
    c_total = 0
    for box in all_boxes:
        if 'sensors' not in box.keys():
            continue
        for sensor in box['sensors']:
            if 'unit' in sensor.keys() and 'lastMeasurement' in sensor.keys():
                if sensor['unit'] == '°C':
                    c_count += 1
                    c_total += float(sensor['lastMeasurement']['value'])

    if c_count == 0:
        return 0
    return c_total/c_count
