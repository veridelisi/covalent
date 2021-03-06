import json
import requests
#Get ERC20 token transfers

host = "https://api.covalenthq.com/"
endpoint = 'v1/{chain_id}/address/{address}/transfers_v2/'
endpoint = endpoint.format(chain_id=43114, address="0x30dfdc78173766ba26127afd1aaaad6e183d8762")

#my adress is 0x30dfdc78173766ba26127afd1aaaad6e183d8762

headers = {
    "cache-control": "public, max-age=10, stale-while-revalidate=30",
    "content-type" : "application/json"
}

parameters = {
    "quote-currency" : "USD",
    #You need to write here contract-address. This is PNG contract address. We will see my PNG transfers.
    "contract-address":"0x60781C2586D68229fde47564546784ab3fACA982",
    "key": "Your KEY"

}

request = requests.get(host + endpoint, headers=headers, params=parameters)

json_data = json.loads(request.text)
json_data_str = json.dumps(json_data, indent=2)

print(json_data_str)
