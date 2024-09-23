import json 
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
industries = []

try:
    with open("industryUnfiltered.json", 'r') as file:
        data = json.load(file)
        print(data)
        for entry in data['results']:
            industries.append(entry['Name'])
        print(industries)
except FileNotFoundError:
    print("The file was not found.")
except json.JSONDecodeError:
     print("Error decoding JSON.")

with open("industryfiltered.json", 'w') as file2:
    json.dump(industries, file2, indent=4)