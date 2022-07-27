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

##Add User
endpoint = f"/{portalname}/users"
headers = {
  'Authorization': 'Bearer ' + myToken
}
payload = '''
        {
    "general_settings": {
    "first_name": "Arthur",
    "last_name": "Miller",
    "object_name": "arthur.miller"
    
  },
  "contact": {
    "email": {
        "work": "arthur.miller@example.org"
    }
  },
  "account": {
    "login_username": "arthur.miller",
  }
}

'''
response = requests.request("POST", url + endpoint, headers=headers, data=payload)
print(response.text)
print(response.headers['Location'])
#getheader('Location'))