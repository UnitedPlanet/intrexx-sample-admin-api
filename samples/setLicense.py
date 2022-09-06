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

##Get Licenses
endpoint = f"/{portalname}/licenses"
headers = {
  'Authorization': 'Bearer ' + myToken
}
payload = '''
        {
          "key": "DB1PZ5BcHYRqnJajrixP772jWxeqWfzkoK8n1MtKUK1m4nvnUyouvoZBvjw45pK7ruDGSLxyejbWSDHZH9RdUPDWRp4t6AAMk8oNd4ZsUJMU",
          "count": 0
        }
        
        '''
response = requests.request("POST", url + endpoint, headers=headers, data=payload)
print(response.text)

