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
    price_l=sorted(list, key=lambda d:d ["platinum"],reverse=True)
    return price_l
    

#list of of all buy and sell sorted into a sellorder var
sellchecker(bs_orders,s_orders)

#sell orders sorted by price asc and lenght for ingame checker
s_p_orders=price_sort_asc(s_orders)
s_p_orders_len = len(s_p_orders)-1

#//to be rewritten as function
#outputs cheapest/newest/online sellorder
while test == false:
    if s_p_orders[s_p_orders_len]["user"]["status"] == "ingame":
        print("Status:    ",s_p_orders[s_p_orders_len]["user"]["status"])
        print("Price:     ",s_p_orders[s_p_orders_len]["platinum"])
        print("Index num: ",s_p_orders_len)
        print("Name:     ",s_p_orders[s_p_orders_len]["user"]["ingame_name"])
        test = true
    else:
        s_p_orders_len-=1