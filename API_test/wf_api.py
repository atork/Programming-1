import requests
import json
from sympy import true,false

input = input("Item name: ")
resp = requests.get('https://api.warframe.market/v1/items/'+input+'/orders')
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
            
#price sorter
def price_sort_asc(list):
    for x in list:
        x+1


sellchecker(bs_orders,s_orders)
s_orders_len = len(s_orders)-1      

#outputs newest available offer
while test == false:
    if s_orders[s_orders_len]["user"]["status"] == "ingame":
        print("Status:    ",s_orders[s_orders_len]["user"]["status"])
        print("Price:     ",s_orders[s_orders_len]["platinum"])
        print("Index num: ",s_orders_len)
        test = true
    else:
        s_orders_len-=1