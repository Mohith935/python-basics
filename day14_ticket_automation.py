# Python API automation with retries and error handling
import requests
import time

URL = "https://jsonplaceholder.typicode.com/posts"
TIMEOUT = 3
RETRIES = 3

def get_posts():
  for attempt in range(RETRIES):
    try:
      response = requests.get(URL, timeout= TIMEOUT)
      if response.status_code == 200:
        print("Posts retrieved successfully")
        return response.json()
    except requests.exceptions.RequestException as e:
      print(f"Attempt {attempt +1} failed:", e)
      time.sleep(2)
  print("All attempts to retrieve posts failed")
  return []

def create_ticket():
  headers = {
    "content-type": "application/json",
    "Accept": "application/json"
  }
  payload = {
    "title": "high cpu usage",
    "body": "high cpu usage",
    "userId": 1
  }
  try:
    response = requests.post(URL, headers= headers, json= payload,timeout= TIMEOUT)
    if response.status_code == 201:
      print("Ticket created: ", response.json())
  except requests.exceptions.RequestException as e:
    print("POST request failed:", e)

posts = get_posts()
filtered_posts = [p for p in posts if p["userId"] == 1]
print("Filtered Posts:", filtered_posts)

create_ticket()