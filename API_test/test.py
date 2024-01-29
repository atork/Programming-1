import requests
import json
from sympy import true,false
import wf_api
#set request
resp = requests.get('https://api.warframe.market/v1/items/mirage_prime_systems')
resp_dicet=resp.json
