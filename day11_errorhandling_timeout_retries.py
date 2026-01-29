# Basic try-except for error handling
import requests
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
  response = requests.get(url)
  print("Status Code:", response.status_code)
  print("Response:", response.json())
except requests.exceptions.RequestException as e:
  print(f"HTTP error occurred: {e}")


# Handling timeout exceptions
import requests
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
  response = requests.get(url, timeout=0.5)
except requests.exceptions.RequestException as e:
  print(f"Request timed out or other error: {e}")


# status code based error handling
import requests
url = "https://jsonplaceholder.typicode.com/invalidendpoint"

response = requests.get(url, timeout=5)
if response.status_code == 200:
  print("Success")
elif response.status_code == 401:
  print("Authentication Error")
elif response.status_code == 404:
  print("Resource Not Found")
elif response.status_code >= 500:
  print("Server Error")
else:
  print("Unexpected Error:", response.status_code)


# Retry logic for transient errors
import requests
import time
url = "https://jsonplaceholder.typicode.com/posts"

for attempts in range(3):
  try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
      print("Success on attempt:",attempts + 1)
      break
    else:
      print("Failed. status code:", response.status_code)
  except requests.exceptions.RequestException as e:
    print(f"Attempt {attempts + 1} failed", e)

else:
  print("All attempts failed")


# Retry logic for transient errors during POST requests
import requests
import time
url = "https:/jsonplaceholder.typicode.com/posts"

payload = {
  "title": "Retry Test",
  "body": "Testing retries",
  "userId": 1
}
for attempts in range(3):
  try:
    response = requests.post(url,json=payload, timeout=3)
    if response.status_code == 201:
      print("POST successful")
      break
    elif response.status_code >= 500:
      print("Server error. Retrying...", response.status_code)
    else:
      print("error:", response.status_code)
  except requests.exceptions.RequestException as e:
    print("error:", e)
    time.sleep(2)