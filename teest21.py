import requests
import json
import os

cache_file = "data_cache.json"
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

if os.path.exists(cache_file):
    with open(cache_file, "r") as f:
        data = json.load(f)
else:
    r = requests.get(url)
    data = r.json()
    with open(cache_file, "w") as f:
        json.dump(data, f, indent=2)

bpi = data["bpi"]
for key, value in bpi.items():
    print("Currency:", key)
    print("Rate:", value["rate"])
    print("Description:", value["description"])
    print("---------------------")
