# Basic python logging
import logging

logging.basicConfig(
  level= logging.INFO,
  format= "%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Script started")
logging.warning("This is a warning")
logging.error("Something went wrong")


# log to a file
import logging

logging.basicConfig(
  filename= "automation.log",
  level= logging.INFO,
  format= "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Script started")
logging.error("API call failed")


# Config files
import json
with open("config.json", "r") as file:
  config = json.load(file)

print(config["api_url"])
print(config["retries"])


# using config, requests, logging
import requests
import json
import logging
import time

logging.basicConfig(
  filename= "automation.log",
  level= logging.INFO,
  format= "%(asctime)s - %(levelname)s - %(message)s",
  force= True
)
logging.info("Logger initialized")


with open("config.json") as f:
  config = json.load(f)

url = config["api_url"]
timeout = config["timeout"]
retries = config["retries"]

for attempt in range(retries):
  try:
    response = requests.get(url, timeout=timeout)
    if response.status_code == 200:
      logging.info("API call successful")
      break
    else:
      logging.warning(f"Unexpected status: {response.status_code}")
  except requests.exceptions.RequestException as e:
    logging.error(f"Attempt {attempt + 1} failed: {e}")
    time.sleep(2)

else:
  logging.critical("All retries failed")


# secrets(Environment Variables)
import os

token = os.getenv("API_TOKEN")
