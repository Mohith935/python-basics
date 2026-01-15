# API BASCIS AND JSON HANDLING
incident = {
  "number": "INC001",
  "status": "open",
  "priority": "high",
  "assigned_to": "IT support"
}
print(incident["number"])
print(incident["priority"])


# JSON module 
import json 
data = {
    "server": "web01",
    "status": "running",
    "cpu": 75
}
# Convert dict to JSON string
json_string = json.dumps(data)
print(json_string)
# Convert JSON string to dict
parsed_data = json.loads(json_string)
print(parsed_data["cpu"])


# Read JSON from a file
with open("day8/incidents.json", "r") as file:
  incidents = json.load(file)
  high_count = 0
  for inc in incidents:
    if inc["priority"] == "High":
      high_count += 1
print("High priority incidents:", high_count)


# incident analyzer
import json

count = {}

with open("day8/incidents.json", "r") as file:
    incidents = json.load(file)
    for inc in incidents:
        priority = inc["priority"]
        count[priority] = count.get(priority, 0) + 1

with open("day8/incident_summary.txt", "w") as file1:
    file1.write("Incident Summary:\n")
    for priority, total in count.items():
        file1.write(f"{priority}: {total}\n")
print("Summary written to incident_summary.txt")