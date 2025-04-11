import json

with open('settings.json') as f:
    d = json.load(f)
    print(d)
