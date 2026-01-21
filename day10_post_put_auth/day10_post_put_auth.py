# post request(create data)
from flask import json
import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
  "title": "server down",
  "body": "server is not responding",
  "userId": 1
}
response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response:", response.json())


# put request(update data)
import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
update_payload = {
  "title": "server down - resolved",
  "body": "issue fixed, server is up now",
  "userId": 1
}
response = requests.put(url, json=update_payload)
print("Status Code:", response.status_code)
print("Updated Response:", response.json())


# API with authentication
from requests.auth import HTTPBasicAuth
import requests
url = "https://httpbin.org/basic-auth/user/pass"
auth = HTTPBasicAuth('user', 'pass')
response = requests.get(url, auth=auth)
print("Status Code:", response.status_code)
print("Secure Data Response:", response.json())


# Header-based authentication
import requests
url = "https://jsonplaceholder.typicode.com/posts"
headers = {
  "Authorization": "Bearer yodummy_token_123",
  "content-type": "application/json"
}
response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)


# 
import json
import requests
url = "https://jsonplaceholder.typicode.com/posts"
headers = {
  "content-type": "application/json",
  "Accept": "application/json"
}
create_payload = {
  "title": "New ticket created",
  "body": "Details of the ticket",
  "userId": 2 
}
create_response = requests.post(url, headers=headers, json=create_payload, timeout=10)
if create_response.status_code == 201:
  print("Ticket created successfully:", create_response.json())
else:
  print("Failed to create ticket.", create_response.status_code)

post_id = create_response.json().get("id")

update_payload = {
  "title": "Updated ticket title",
  "body": "Updated details of the ticket",
  "userId": 2
}
update_response = requests.put(f"{url}/{post_id}", headers=headers, json=update_payload, timeout=10)
if update_response.status_code == 200:
  print("Ticket updated successfully:", update_response.json())
else:
  print("Failed to update ticket.", update_response.status_code)