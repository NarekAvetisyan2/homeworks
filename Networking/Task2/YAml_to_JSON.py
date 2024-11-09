import yaml
import json

from yaml import Loader

with open("yaml_to_json.yaml", "r") as yaml_file:
    yaml_data = yaml.load(yaml_file, Loader)

with open("yaml_to_json.json", "w") as json_file:
    json.dump(yaml_data, json_file, indent = 3)