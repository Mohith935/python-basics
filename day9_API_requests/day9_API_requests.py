import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print("Status Code:", response.status_code)
print(response.text[:300])


# convert response to JSON
import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

data = response.json()
print(type(data))
print(data[0])
print("First Post Title:", data[0]["title"])
print("Total Posts Retrieved:", len(data))


# loop through API data
import json
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
for post in data[:5]:
  print("Post ID:", post["id"], "Title:", post["title"])


# Filter API data
import json
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
for post in data:
  if post["userId"] == 1:
    print("Post ID:", post["id"], "Title:", post["title"])
# Save API data to a file
with open("posts.json", "w") as file:
  json.dump(data, file, indent=4)
print("Posts saved to posts.json")


# Script to fetch posts from API and count posts per user
import json
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
user_post_count = {}
for post in data:
  user_id = post["userId"]
  if user_id in user_post_count:
    user_post_count[user_id] += 1
  else:
    user_post_count[user_id] = 1
with open("user_post_summary.txt", "w") as file:
  file.write("Number of Posts per User:\n")
  for user_id, count in user_post_count.items():
    file.write(f"User {user_id}: {count} posts\n")