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

##Create Portal
endpoint = f"/portals"
headers = {
  'Authorization': 'Bearer ' + myToken
}
payload = '''
        {
    "template_path": "/opt/intrexx/orgtempl/blank/",
    "portal_path": "/opt/intrexx/org/mytest",
    "portal": {
    "display_name": "mytest",
    "default_language": "de",
    "web_server_host_name": "localhost",
    "web_default_base_url": "https://localhost:1337",
    "web_connector_host": "localhost",
    "web_connector_port": 1337,
    "rest_connector_port": 8101,
    "search_configuration": {
      "server_configuration": {
      "url": "http://localhost:8983",
      "base_directory": "/opt/intrexx/solr/server/solr"
      }
    }
  },
  "database": {
    "port": 5432,
    "host": "localhost",
    "user": "postgres",
    "password": "secret",
    "database_name": "ixmytest",
    "create": true,
    "type": "postgresql"
  }
}

'''
response = requests.request("POST", url + endpoint, headers=headers, data=payload)
print(response.text)