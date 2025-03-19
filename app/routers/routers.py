"""Main Router for the api"""
from fastapi import APIRouter
from app.config.settings import settings
import requests
from datetime import datetime , timezone , timedelta
import numpy as np
from prometheus_client import CollectorRegistry , generate_latest , CONTENT_TYPE_LATEST
from starlette.responses import Response


router = APIRouter()

@router.get("/version")
def version_printing():
    """
    Printing the version of the api
    """
    return {"version":settings.VERSION}

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
    reads_mean = np.mean(reads)
    if reads_mean <= 10 :
        reads_status = "Too Cold"
    elif (reads_mean > 11 and reads_mean <= 36):
        reads_status = "Good"
    else:
        reads_status = "Too Hot"
    return {"The average Temperature of the SenseBoxes":reads_mean,"The Status of temperature":reads_status}

@router.get('/metrics')
def prom_defualt_metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)