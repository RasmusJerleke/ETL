import json
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import globals

# 2. Write a function that reads the JSON files from data/testing/raw and transforms it to a 
# list of tuples, then returns this list together with the keys from the JSON object.
def read_json():
    with open(globals.RAW_DATA_PATH, 'r') as f:
        data = json.load(f)
    return [x for x in data.items()], data.keys()

# write another function that takes as inputs a list of tuples, a list of strings, and a filepath. 
# The function should write the list as a JSON object to file.
def write_to_file(tuple_list, strings, filepath=globals.HARMONIZED_DATA_PATH):
    dict = {t[0] : t[1] for t in tuple_list}
    with open(filepath, 'w') as f:
        json.dump(dict, f, indent=4)
