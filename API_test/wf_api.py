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
#price sorter after ky with lambda(no idea how lambda works)
def price_sort_asc(list):
    price_l=sorted(list, key=lambda d:d ["platinum"])
    return price_l
#ingame sorter
def online(list):
    lenghtl=len(list)
    for x in list:
        if x["user"]["status"]=="ingame":
            return x


#//programstart  
#list of of all buy and sell sorted into a sellorder var
sellchecker(bs_orders,s_orders)

#sell orders sorted by price asc and lenght for ingame checker
s_p_orders=price_sort_asc(s_orders)

#puts online orders in x
final_order=online(s_p_orders)

jprint(final_order)


