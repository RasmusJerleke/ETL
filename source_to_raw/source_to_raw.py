import requests
# Write a function that does a request to a URL and returns the resource as a Python dict.
def get_request(url:str) -> dict:
    try:
        return requests.get(url).json()
    except:
        return None
