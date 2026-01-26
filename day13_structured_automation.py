""" Day 13: Structured automation script

- Refactored to follow clean automation patterns
- Uses main() as entry point
- Modular functions for configuration, API calls, and logging
- It can be reused and extended easily
"""

import logging
import json
import requests
import time

LOG_FILE = "automation.log"
CONFIG_FILE = "config.json"

def logging_setup():
  logging.basicConfig(
    filename= LOG_FILE,
    level= logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s"
  )

def load_config():
  with open(CONFIG_FILE, "r") as file:
    return json.load(file)
  
def api_call(url, timeout, retries):
  for attempt in range(1, retries + 1):
    try:
      response = requests.get(url, timeout=timeout)
      response.raise_for_status()
      logging.info(f"API call successful on attempt {attempt}")
      return response.json()
    except requests.RequestException as e:
      logging.error(f"Attempt {attempt} failed: {e}")
      time.sleep(2)
  logging.critical("All reteries failed")
  return None

def main():
  logging_setup()
  logging.info("Script started")
  config = load_config()
  url = config["api_url"]
  timeout = config["timeout"]
  retries = config["retries"]
  data = api_call(url, timeout, retries)
  if data:
    logging.info("Received data")
  else:
    logging.error("No data received from API")

  logging.info("Script ended")

if __name__ == "__main__":
  main()