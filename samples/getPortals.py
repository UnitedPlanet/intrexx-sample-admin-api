##Imports
import requests
import json

##Definitions
url = "https://localhost:4242"
name = "admin"
password = "p4$sworD"

##Auth
payload = json.dumps({
  "name": name,
  "password": password
})
headers = {
  'Content-Type': 'application/json'
}
endpoint = "/auth"
response = requests.request("POST", url + endpoint, headers=headers, data=payload)
myToken = response.text

##get Portals
endpoint = "/portals"
headers = {
  'Authorization': 'Bearer ' + myToken
}
response = requests.request("GET", url + endpoint, headers=headers)
print(response.text)
