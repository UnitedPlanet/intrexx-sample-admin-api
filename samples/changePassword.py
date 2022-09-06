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

##change Password for User with ID 6
userID = "6"
endpoint = f"/{portalname}/users/{userID}"
headers = {
  'Authorization': 'Bearer ' + myToken
}
payload = '''{
"account": {
    "password": "secret"
  }
}
'''
response = requests.request("PATCH", url + endpoint, headers=headers, data=payload)
print(response.text)

