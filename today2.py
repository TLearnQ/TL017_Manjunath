import json

data = [
    {"id": 1, "region": "east"},
    {"id": 2, "region": "west"},
    {"id": 3, "region": "east"}
]

east = []
west = []

for obj in data:
    if obj["region"] == "east":
        east.append(obj)
    else:
        west.append(obj)

with open("sensor.json", "w") as f:
    json.dump(east, f, indent=2)
with open("sensor.json", "w") as f:
    json.dump(west, f, indent =2)

print("json file created successfully")

