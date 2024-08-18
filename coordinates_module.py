import json
import urllib.request
from geopy.geocoders import Nominatim

def get_coordinates():
    # Cargar el estado actual de la ISS en tiempo real
    response = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")
    result = json.loads(response.read())

    # Extraer la ubicación y hora de la ISS
    location = result["iss_position"]
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    time = result["timestamp"]

    return lon, lat, time

def getloc(lon, lat):
    geolocator = Nominatim(user_agent="ISS Tracker")
    location = geolocator.reverse(f'{lat},{lon}')
    if location is None:
        return 'Océano'
    return location.raw['address'].get('country', '')
