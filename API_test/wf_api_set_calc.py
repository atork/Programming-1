import wf_api
import requests
import json
from sympy import true,false
import pandas

input = input("Warframe name: ")
fullnam= input+"_prime"

wf_blueprint=fullnam+"_blueprint"
wf_sys=fullnam+"_systems"
wf_neuro=fullnam+"_neuroptics"
wf_chassis=fullnam+"_chassis"

#Singleparts 
#request and unpacking
resp = requests.get('https://api.warframe.market/v1/items/'+wf_blueprint+'/orders')
blue_resp_dict = resp.json()
blue_sb=wf_api.depacker(blue_resp_dict)
resp = requests.get('https://api.warframe.market/v1/items/'+wf_sys+'/orders')
sys_resp_dict = resp.json()
sys_sb=wf_api.depacker(sys_resp_dict)
resp = requests.get('https://api.warframe.market/v1/items/'+wf_neuro+'/orders')
neuro_resp_dict = resp.json()
neuro_sb=wf_api.depacker(neuro_resp_dict)
resp = requests.get('https://api.warframe.market/v1/items/'+wf_chassis+'/orders')
chassis_resp_dict = resp.json()
chassie_sb=wf_api.depacker(chassis_resp_dict)
#sorting for sell orders
blue_s=[]
wf_api.sellchecker(blue_sb,blue_s)
sys_s=[]
wf_api.sellchecker(sys_sb,sys_s)
neuro_s=[]
wf_api.sellchecker(neuro_sb,neuro_s)
chassis_s=[]
wf_api.sellchecker(chassie_sb,chassis_s)
#price sorting
blue_s_asc=wf_api.price_sort_asc(blue_s)
sys_s_asc=wf_api.price_sort_asc(sys_s)
neuro_s_asc=wf_api.price_sort_asc(neuro_s)
chassis_s_asc=wf_api.price_sort_asc(chassis_s)
#ingame sort fin
blue=wf_api.ingame(blue_s_asc)
sys=wf_api.ingame(sys_s_asc)
neuro=wf_api.ingame(neuro_s_asc)
chassis=wf_api.ingame(chassis_s_asc)
#single calc
print("Singleprice: ",end="")
print(wf_api.price(blue)+wf_api.price(sys)+wf_api.price(neuro)+wf_api.price(chassis))

#set request
setnam=fullnam+"_set"
resp = requests.get('https://api.warframe.market/v1/items/'+setnam+'/orders')
resp_dict=resp.json
resp_sb=wf_api.depacker(resp_dict)
resp_s=[]
wf_api.sellchecker(resp_sb,resp_s)
res_s_asc=wf_api.price_sort_asc(resp_s)
res_ord=wf_api.ingame(res_s_asc)
print(wf_api.price(res_ord))
