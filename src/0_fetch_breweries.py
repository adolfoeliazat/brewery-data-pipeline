import requests

def fetch_breweries():
    url = "https://api.openbrewerydb.org/breweries"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data from API: {response.status_code}")
