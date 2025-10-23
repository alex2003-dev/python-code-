import json

settings = {
    "speed": "medium",
    "retries": 3
}

try:
    with open("config.json", 'r') as f:
        conf = json.load(f)
        settings.update(conf)
except FileNotFoundError:
    pass
except json.JSONDecodeError:
    pass
except Exception:
    pass