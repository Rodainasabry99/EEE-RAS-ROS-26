import json

def save_inventory(data):
    with open("inventory.json", "w") as f:
        json.dump(data, f)

def load_inventory():
    try:
        with open("inventory.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

data = {"apple": 10, "banana": 5}
save_inventory(data)

print(load_inventory())