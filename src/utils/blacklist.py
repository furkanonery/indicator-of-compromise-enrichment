import requests
from src.configs.config import GOOGLE_SAFE_BROWSING_API_KEY

def is_blacklisted(url):
    safebrowsing_url = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

    payload = {
        "client": {
            "clientId": "your-client-id",
            "clientVersion": "1.5.2",
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}],
        },
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GOOGLE_SAFE_BROWSING_API_KEY}",
    }

    response = requests.post(safebrowsing_url, json=payload, headers=headers)
    if response.ok:
        data = response.json()
        if "matches" in data and data["matches"]:
            return True
    return False