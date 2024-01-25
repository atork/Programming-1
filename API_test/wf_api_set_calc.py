import wf_api
import requests
import json
from sympy import true,false

input = input("Warframe name: ")
fullnam= input+"_prime"

wf_blueprint=fullnam+"_blueprint"
wf_sys=fullnam+"_systems"
wf_neuro=fullnam+"_neuroptics"
wf_chassie=fullnam+"_chassie"

resp = requests.get('https://api.warframe.market/v1/items/'+wf_blueprint+'/orders')
blue_resp_dict = resp.json()
blue_sb=wf_api.depacker(blue_resp_dict)
resp = requests.get('https://api.warframe.market/v1/items/'+wf_sys+'/orders')
sys_resp_dict = resp.json()
sys_sb=wf_api.depacker(sys_resp_dict)
resp = requests.get('https://api.warframe.market/v1/items/'+wf_neuro+'/orders')
neuro_resp_dict = resp.json()
neuro_sb=wf_api.depacker(neuro_resp_dict)
resp = requests.get('https://api.warframe.market/v1/items/'+wf_chassie+'/orders')
chassie_resp_dict = resp.json()
#depacker for chassie not working key error???
chassie_sb=wf_api.depacker(chassie_resp_dict)


blue_s=[]
wf_api.sellchecker(blue_sb,blue_s)
wf_api.jprint(blue_s)