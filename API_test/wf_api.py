import requests
import json
from sympy import true,false



#json printer
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
def depacker(dict):
    return dict["payload"]["orders"]
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
