import json


with open("Creat_JSON.json") as old_file:
    old_data = json.load(old_file)

with open("Creat_JSON_new.json", "w") as new_file:
    json.dump(old_data, new_file, indent = 4)