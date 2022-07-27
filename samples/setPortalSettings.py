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

##Get MailService
endpoint = f"/{portalname}/settings"
headers = {
  'Authorization': 'Bearer ' + myToken
}
payload = '''       
    {
        "jvm_minimal_memory_mb":512,
        "anonymous_session_timeout_sek":3600,
        "workflow_event_on_login":true,
        "session_timeout_sek":3600,
        "jvm_maximal_memory_mb":1024}
'''
response = requests.request("PATCH", url + endpoint, headers=headers, data=payload)
print(response.text)
print(response.headers)
