import requests
import json
from sympy import false, true

resp = requests.get('https://api.warframe.market/v1/items/ash_prime_blueprint/orders')
resp_dict = resp.json()
bs_orders = resp_dict["payload"]["orders"]
bs_orders_len = len(bs_orders)-1
test = false

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#outputs newest available offer for ash blueprint
while test == false:
    if bs_orders[bs_orders_len]["user"]["status"] == "ingame":
        print("Status:    ",bs_orders[bs_orders_len]["user"]["status"])
        print("Price:     ",bs_orders[bs_orders_len]["platinum"])
        print("Index num: ",bs_orders_len)
        test = true
    else:
        bs_orders_len-=1
