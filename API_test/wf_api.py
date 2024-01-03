
import requests
import json
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



resp = requests.get('https://api.warframe.market/v1/items/primed_convulsion')
resp_dict = resp.json()

print(resp_dict.get('page'))

