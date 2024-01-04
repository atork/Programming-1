
import requests
import json
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



resp = requests.get('https://api.warframe.market/v1/items/ash_prime_blueprint/orders')
resp_dict = resp.json()

#prints out the oldest sell/buy-orders
#jprint(str(resp_dict["payload"]["item"]["items_in_set"][0]["en"]["description"]))
jprint(resp_dict["payload"]["orders"][0]["creation_date"])
jprint(resp_dict["payload"]["orders"][1]["creation_date"])
jprint(resp_dict["payload"]["orders"][2]["creation_date"])
jprint(resp_dict["payload"]["orders"][3]["creation_date"])
jprint(resp_dict["payload"]["orders"][4]["creation_date"])

