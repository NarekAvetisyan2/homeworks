import yaml
from yaml import Loader

with open("config.yaml") as f:
    res = yaml.load(f, Loader)

res["server"]["port"] = 9090

with open("config.yaml", "w") as f:
    yaml.dump(res, f)

print(res)