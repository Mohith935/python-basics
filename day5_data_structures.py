# List
tickets = ["INC001", "INC002", "INC003"]
print(tickets)
print(tickets[0])
print(len(tickets))
# Modifying list
tickets.append("INC004") 
tickets.remove("INC003")
for ticket in tickets:
  print(ticket)


# Tuple(Ordered and Immutable of items)
server = ("web01", "running", 80)
print(server[0])
print(server[1])
print(len(server))


# Dictionary(Key-Value pairs)
incident = {
  "number": "INC001",
  "status": "open",
  "priority": "high"

}
# will raise a KeyError if "number" is missing.
print(incident["number"])
# returns None (or a default value you provide) if the key is missing.
print(incident.get("status", "not found"))
# Modifying dictionary
incident["assigned_to"] = "IT Team"
incident["status"] = "In progress"
for key, value in incident.items():
  print(key, ":", value)


# list of dictionaries
incidents = [
  {"number": "INC001", "status": "open"},
  {"number": "INC002", "status": "closed"},
  {"number": "INC003", "status": "in progress"}
]
for inc in incidents:
  print(inc["number"], "is", inc["status"])


# SET(Unordered collection of unique items, it removes duplicates)
users = {"admin", "john", "admin", "alice"}
print(users)


# incident priority counter
incidents = [
  {"priority": "high"},
  {"priority": "low"},
  {"priority": "high"},
  {"priority": "medium"},
  {"priority": "high"}
]
priority_count = {"high": 0, "medium": 0, "low": 0}
for inc in incidents:
  if inc[priority] == "high":
    priority_count["high"] += 1
  elif inc[priority] == "medium":
    priority_count["medium"] += 1
  elif inc[priority] == "low":
    priority_count["low"] += 1
# Alternative approach
  priority = inc["priority"]
  priority_count[priority] += 1
print(priority_count)
print("Number of high priority incidents:", priority_count["high"])
