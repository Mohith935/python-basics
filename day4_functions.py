def greet():
  return "Hello, World!"
print(greet())


# Function with parameters
def greet_user(name):
  print("Hello,", name)
greet_user("Ram")
greet_user("rajitha")


# return statement(sends back a value)
def add(a, b):
  return a + b
result = add(5, 7)
print("sum is:", result)


# CPU Alert Function
def cpu_alert(usage):
  if usage > 80:
    return "CRITICAL"
  elif usage > 60:
    return "HIGH"
  else:
    return "NORMAL"
status = cpu_alert(75)
print("CPU Usage Status:", status)


# Login Validator Function
def login_validation(username, password):
  if username == "admin" and password == "admin123":
    return "Access Granted"
  else:
    return "Access Denied"
result = login_validation("admin", "admin123")
print(result)
