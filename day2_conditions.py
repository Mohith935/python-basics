a = 10
b = 20

# Comparison & Logical Operators
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

print( a < b and b > 15)
print(a > b or b > 15)

# Even or Odd
num = int(input("Enter a number:"))
if num % 2 == 0:
  print("Even number")
else:
  print("Odd number")

# Login Validation
username = input("Enter username:")
password = input("Enter password:")
if username == "admin" and password == "1234":
  print("Login successful")
else:
  print("Invalid credentials")


  # Alert System
  cpu_usage = int(input("Enter CPU usage:"))
  if cpu_usage > 80:
    print("High cpu usage alert!")
  elif cpu_usage > 60:
    print("Moderate cpu usage warning.")
  else:
    print("CPU usage normal.")

# Number Sign Checker
number = int(input("Enter a number:"))
if number > 0:
  print("Positive number")
elif number < 0:
  print("Negative number")
else:
  print("Zero")


# Largest of Three Numbers
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
if num1 >= num2 and num1 >= num3:
  print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
  print("Largest number is:", num2)
else:
  print("Largest number is:", num3)


# Age Category System
age = int(input("Enter your age:"))
if age < 13:
  print("Child")
elif age <= 19:
  print("Teen")
elif age <= 59:
  print("Adult")
else:
  print("Senior")


# Simple ATM Logic
balance = 10000
withdrawal_amount = int(input("Enter withdrawal amount:"))
if withdrawal_amount > balance:
  print("Insufficient funds")
else:
  balance = balance - withdrawal_amount
  print("Remaining balance:", balance)


# Exam Result System
marks = int(input("Enter your marks:"))
if marks < 35:
  print("Fail")
elif marks < 60:
  print("Pass")
elif marks < 85:
  print("First Class")
else:
  print("Distinction")


# Login + Role Check
username = input("Enter username:")
password = input("Enter password:")
if username == "admin" and password == "admin123":
  role = input("Are you an admin or user?")
  if role == "admin":
    print("Full access granted")
  elif role == "user":
    print("Limited access granted")
  else:
    print("Invalid role")
else:
  print("Invalid credentials")


# Login + Role Check
# Requirement:
# Username = admin
# Password = admin123
# If login correct:
# Ask role (user / admin)
# Print access level
# 💡 Used in real systems.



