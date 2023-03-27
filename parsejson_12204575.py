import json
import yaml

with open('myfile_12204575.json', 'r') as json_file:
	ourjson = json.load(json_file)

print(ourjson)
