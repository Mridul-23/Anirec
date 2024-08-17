# This file here will be responsible for merging various json files inton a single json file

import json
import os

# Directory containing .json files
directory = r'C:\Users\HP\Desktop\Anirec\Raw scrapped files'

# List to hold combined data
combined_data = []

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        filepath = os.path.join(directory, filename)
        
        # Read and parse JSON data with specified encoding
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            combined_data.append(data)

# Write combined data to a new .json file
with open('combined.json', 'w', encoding='utf-8') as outfile:
    json.dump(combined_data, outfile, indent=4, ensure_ascii=False)

print('JSON files combined successfully!')
