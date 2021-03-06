
import json
import requests
#Get Log events by topic hash(es) 

host = "https://api.covalenthq.com/"
endpoint = 'v1/{chain_id}/events/topics/{topic}/'
endpoint = endpoint.format(chain_id=43114, topic="0x4c209b5fc8ad50758f13e2e1088ba56a560dff690a1c6fef26394f4c03821c4f")
                           
#This is topic of minting PGL. 0x4c209b5fc8ad50758f13e2e1088ba56a560dff690a1c6fef26394f4c03821c4f 
headers = {
    "cache-control": "public, max-age=10, stale-while-revalidate=30",
    "content-type" : "application/json"
}

parameters = {
    #Blocks numbers'
    "starting-block": "2547634",
    "ending-block": "latest",
    "quote-currency" : "USD",
   
    "key":"Your KEY"
    
    
}



request = requests.get(host + endpoint, headers=headers, params=parameters)

json_data = json.loads(request.text)
json_data_str = json.dumps(json_data, indent=2)

print(json_data_str)


#Transactions' names and amounts
for transactions in json_data["data"]["items"]:
   
        names=transactions["decoded"]["name"]
        values=transactions["decoded"]["params"][-1]["value"]
        print(names,values)
        
#Pool address and Deposited amounts to the pools      
for transactions in json_data["data"]["items"]:
   
        names=transactions["decoded"]["name"]
        values=[param["value"] for param in transactions["decoded"]["params"]]
        print(names,values)  
        
#Deposited amounts to the pools        
for transactions in json_data["data"]["items"]:
  
        names=transactions["decoded"]["name"]
        values=[(param["name"],param["value"]) for param in transactions["decoded"]["params"] if param["type"] !="address"]
        print(names,values)      
        
        
