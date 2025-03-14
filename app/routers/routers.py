from fastapi import APIRouter
from app.config.settings import settings
import requests
from datetime import datetime , timezone , timedelta
import numpy as np

router = APIRouter()

@router.get("/version")
def version_printing():
    """
    Printing the version of the api
    """
    return {"veriosn":settings.VERSION}

@router.get("/temperature")
def get_average_temperature():
    """
    return the average temperature of all senseboxes
    """
    start_time = (datetime.now(timezone.utc) - timedelta(hours=1))
    # Format the datetime object to match the desired format
    start_time = start_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-4] + 'Z'
    till_time = (datetime.now(timezone.utc))
    till_time = till_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-4] + 'Z'
    params={
        "bbox":"-180.0,-90.0,180.0,90.0",
        "phenomenon":"temperature",
        "from-date":start_time,
        "to-date":till_time,
        "operation":"  geometricMean",
        "download":"false",
        "format":"json",
        "window":"1 hour"
    }
    response = requests.get("https://api.opensensemap.org/statistics/descriptive",params=params)
    reads = []
    for sensor in response.json():
        for key in sensor.keys():
            if 'sensorId' in key:
                pass
            else:
                reads.append(sensor[key])
    return {"The average Temperature of the SenseBoxes":np.mean(reads)}
