pip install httpclient

import http.client
import json

conn = http.client.HTTPSConnection("api.covalenthq.com")
payload = ''
headers = {
  'Authorization': 'Basic Y2tleV86'
}
conn.request("GET", "/v1/43114/events/topics/0x4c209b5fc8ad50758f13e2e1088ba56a560dff690a1c6fef26394f4c03821c4f,0xdccd412f0b1252819cb1fd330b93224ca42612892bb3f4f789976e6d81936496,0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822/?starting-block=2293594&ending-block=latest", payload, headers)
#We put 3 different topics thanks to this code

res = conn.getresponse()
json_data = res.read()
json_data = json.loads(json_data)
json_data_str = json.dumps(json_data, indent=2)

print(json_data_str)


#There are 100 transactions
len(json_data["data"]["items"])

#Names
contract_names = []

for item in json_data["data"]["items"]:
    contract_names.append(item["decoded"]["name"])

contract_names



#WE count topic's numbers
print("Swap :" ,contract_names.count("Swap"))
print("Mint :" ,contract_names.count("Mint"))
print("Burn:" ,contract_names.count("Burn"))
print("All transactions : ",contract_names.count("Swap") +contract_names.count("Mint")+contract_names.count("Burn"))



#Names and amounts
for transactions in json_data["data"]["items"]:
   
      names=transactions["decoded"]["name"] 
      values=[param["value"] for param in transactions["decoded"]["params"]]
        
      print(names,values)
      
      
      
#Names and amounts      
      
for transactions in json_data["data"]["items"]:
   
        names=transactions["decoded"]["name"]
        values=[(param["name"],param["value"]) for param in transactions["decoded"]["params"]]
        print(names,values)
        
      
#Names and amounts        
for transactions in json_data["data"]["items"]:
  
        names=transactions["decoded"]["name"]
        values=[(param["name"],param["value"]) for param in transactions["decoded"]["params"] if param["type"] !="address"]
        print(names,values)
        
        
        



