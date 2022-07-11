import requests
import json
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import globals

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

def run(url, path =globals.RAW_DATA_PATH):
    dict = get_request(url)
    if dict == None:
        return False
    return create_json_file (dict, path)


run('https://swapi.dev/api/people/1', 'data/test/raw/data.json')