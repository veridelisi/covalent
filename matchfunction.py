import json
import requests
#Get transactions with match function

host = "https://api.covalenthq.com/"
endpoint = 'v1/{chain_id}/address/{address}/transactions_v2/'
endpoint = endpoint.format(chain_id=1, address="0x7A15f704d45AADA83F18ac81b41EaCD48f766E90")

headers = {
    "cache-control": "public, max-age=10, stale-while-revalidate=30",
    "content-type" : "application/json"
}

parameters = {
  
    "match" : '[{"$match":{"gas_price":41000000000}}]',
    "key":"Your KEY"  
}

request = requests.get(host + endpoint, headers=headers, params=parameters)

json_data = json.loads(request.text)
json_data_str = json.dumps(json_data, indent=2)

print(json_data_str)
