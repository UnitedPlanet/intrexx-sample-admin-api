##Imports
import requests
import json

##Definitions
url = "https://localhost:4242"
name = "admin"
password = "p4$sworD"
portalname = "test01"

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
headers = {
  'Authorization': 'Bearer ' + myToken
}

##Delete User with the ID 6
userID = 6
endpoint = f"/{portalname}/users/{userID}"
response = requests.request("DELETE", url + endpoint, headers=headers)

print(response)