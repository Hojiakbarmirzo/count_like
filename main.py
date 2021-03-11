import requests
import json
from pprint import pprint

def countLike(like):
    global l
    global d
    if like=="👍":
        l+=1
    elif like=="👎":
        d=d+1
    print(l,d)

    
token='1696683157:AAH3NeNVQfFeIwBQtBCAokCOb2hp9_773SQ'

def getUpdates():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    r=requests.get(url)
    data=r.json()
    updates=data['result']
    return updates


temp=len(getUpdates())
like="👍"
dislike="👎"
l=0
d=0
while True:
    if temp != len(getUpdates()):
        temp=len(getUpdates())
        update=getUpdates()[temp-1]
        xat=update['message']
        user=xat['from']
        user_id=user['id']
        text=xat.get('text',"")
        countLike(text)
     
        
        

        
   

    

