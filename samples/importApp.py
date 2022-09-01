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

##Import
endpoint = f"/{portalname}/applications"

payload={}
files=[
  ('files',('myApp.zip',open('C:/tmp/myApp.zip','rb'),'application/zip'))
]
headers = {
  'Authorization': 'Bearer ' + myToken
}
response = requests.request("POST", url + endpoint, headers=headers, data=payload, files=files)
print(response.text)