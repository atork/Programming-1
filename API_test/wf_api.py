from turtle import done
import requests
import json
from sympy import false, true

resp = requests.get('https://api.warframe.market/v1/items/ash_prime_blueprint/orders')
resp_dict = resp.json()
bs_orders = resp_dict["payload"]["orders"]
s_orders = []
test = false
#json printer
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#sellorder checker
def sellchecker(list,slist):
    for x in list:
        if x["order_type"] == "sell":
            slist.append(x)
            print("hello")
           
sellchecker(bs_orders,s_orders)
s_orders_len = len(s_orders)-1      

#outputs newest available offer for ash blueprint
while test == false:
    if s_orders[s_orders_len]["user"]["status"] == "ingame":
        print("Status:    ",s_orders[s_orders_len]["user"]["status"])
        print("Price:     ",s_orders[s_orders_len]["platinum"])
        print("Index num: ",s_orders_len)
        test = true
    else:
        s_orders_len-=1

