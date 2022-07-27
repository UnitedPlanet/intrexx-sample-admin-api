##Imports
import requests
import json

##Definitions
url = "https://irmatest.myintrexx.de/irma"
name = "admin"
password = "intrexx"
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
        
'''
response = requests.request("GET", url + endpoint, headers=headers, data=payload)
print(response.text)
print(response.headers)
