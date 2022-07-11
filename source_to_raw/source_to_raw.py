import requests
import json

# Write a function that does a request to a URL and returns the resource as a Python dict.
def get_request(url:str) -> dict:
    try:
        return requests.get(url).json()
    except:
        return None

def create_json_file(dict, path):
    if dict == None:
        return False
    with open(path, 'w') as f:
        json.dump(dict, f, indent=4)
    return True
