import requests

def is_ssl_enabled(url):
    try:
        response = requests.get(url)
        return response.url.startswith("https")
    except requests.exceptions.RequestException:
        return False
