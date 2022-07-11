import os
root = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
full_path = lambda p : os.path.join(root, p)
dirs = ['data/test/harmonized', 'data/test/raw', 
        'cleansed_to_curated', 'harmonized_to_cleansed',
        'raw_to_harmonized', 'source_to_raw']
[os.makedirs(full_path(dir)) for dir in dirs if not os.path.isdir(full_path(dir))]