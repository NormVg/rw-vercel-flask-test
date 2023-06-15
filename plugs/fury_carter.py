import requests
import json
from plugs.config import carter_key
# from config import carter_key
def ask_fury(com,user, key=None):
    if key == None : key = carter_key
    response = requests.post("https://api.carterlabs.ai/chat", headers={
        "Content-Type": "application/json"
    }, data=json.dumps({
        "text": f"{user}: {com}",
        "key": key,
        "playerId": f"{user}" # THIS CAN BE ANYTHING YOU WANT!

    }))
    force_behav = response.json()['forced_behaviours']
    res = response.json()['output']["text"]
#print(response.json())
    if len(force_behav) >0:
        return  res,force_behav[0]['name']
    else:
        return res, ""

# print(ask_fury("tell space news fury","

