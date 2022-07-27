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

##Get SchedulerJobs
endpoint = f"/{portalname}/scheduler/jobs"
headers = {
  'Authorization': 'Bearer ' + myToken
}
payload = '''
        
'''
response = requests.request("GET", url + endpoint, headers=headers, data=payload)
print(response.text)
print(response.headers)