import socket
from geopy.geocoders import Nominatim
import json

def get_geometric_location(url):
    # Resolving URL to IP address
    ip_address = socket.gethostbyname(url)

    # Converting IP address to geolocation
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(ip_address, language="en")

    if location:

        data = {
            "url": url,
            "ip_address": ip_address,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "address": location.address,
        }

        json_data = json.dumps(data)

        return json_data
    else:
        data = {
            "url": url,
            "ip_address": ip_address,
            "error": "Geometric location not found for this IP address.",
        }


        json_data = json.dumps(data)

        return json_data