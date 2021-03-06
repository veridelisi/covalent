import json
import requests
#Get a block

host = "https://api.covalenthq.com/"
endpoint = 'v1/{chain_id}/block_v2/{block_height}/'
#You need to write block_height number to the following block_height section
endpoint = endpoint.format(chain_id=43114, block_height="2254932")

headers = {
    "cache-control": "public, max-age=10, stale-while-revalidate=30",
    "content-type" : "application/json"
}

parameters = {
    
    "quote-currency" : "USD",
    "key": "Your KEY"
  
}

request = requests.get(host + endpoint, headers=headers, params=parameters)

json_data = json.loads(request.text)
json_data_str = json.dumps(json_data, indent=2)

print(json_data_str)
