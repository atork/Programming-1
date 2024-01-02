import requests
import json
response = requests.get("https://api.warframe.market/v1/items/mirage_prime_systems")
print(response.json)


def jsonprint(obj):
    
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jsonprint(response.json())
