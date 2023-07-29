import whois
import json
from datetime import datetime

def convert_datetime(obj):
    if isinstance(obj, datetime):
        return obj.__str__()

def get_whois_info(domain):
    try:
        whois_info = whois.whois(domain)
        data = whois_info
        json_data = json.dumps(data, default=convert_datetime)

        return json_data
    except Exception as e:
        return str(e)