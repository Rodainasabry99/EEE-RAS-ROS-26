import json

try:
    with open("config.json", "r") as file:
        data = json.load(file)
    print("System Ready")

except FileNotFoundError:
    default_data = {
        "name": "default_system",
        "version": 1.0
    }

    with open("config.json", "w") as file:
        json.dump(default_data, file)

    print("File not found → Created default config file")