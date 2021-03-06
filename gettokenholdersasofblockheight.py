import json
import requests
#Get  token holders as of a block height 

host = "https://api.covalenthq.com/"
endpoint = 'v1/{chain_id}/tokens/{address}/token_holders/'
endpoint = endpoint.format(chain_id=43114, address="0x60781C2586D68229fde47564546784ab3fACA982")

#This is Png 0x60781C2586D68229fde47564546784ab3fACA982
                           

headers = {
    "cache-control": "public, max-age=10, stale-while-revalidate=30",
    "content-type" : "application/json"
}

parameters = {
    #Blocks numbers'
    "block-height": "latest",
    
    "quote-currency" : "USD",
   
    "key":"Your KEY"
    
    
}



request = requests.get(host + endpoint, headers=headers, params=parameters)

json_data = json.loads(request.text)
json_data_str = json.dumps(json_data, indent=2)

print(json_data_str)



#Token holders and their balances
for transactions in json_data["data"]["items"]:
   
        names=transactions["address"]
        values=transactions["balance"]
        print(names,values)
