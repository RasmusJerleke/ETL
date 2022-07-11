import requests
import json

# Write a function that does a request to a URL and returns the resource as a Python dict.
def get_request(url:str) -> dict:
    try:
        return requests.get(url).json()
    except:
        return None

def create_json_file(dict, path):
    with open(path, 'w') as f:
        json.dump(dict, f, indent=4)
    return True

def run(url, path = 'data/test/raw/data.json'):
    dict = get_request(url)
    if dict == None:
        return False
    return create_json_file (dict, path)



