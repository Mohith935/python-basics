# Loops
# print numbers from 1 to 10 using a for loop
for i in range(1, 11):
  print(i)


# Print Even Numbers
for i in range(2, 51, 2):
  print("even numbers",i)


# Sum of Numbers
num = int(input("Enter a number:"))
sum = 0
for i in range(1, num+1):
  sum+= i
print("Sum of numbers is:", sum)


# Multiplication Table
num = int(input("Enter a number to print its multiplication table:"))
for i in range(1, 11):
  print(num, "x", i, "=", num*i)


# Password Retry System
correct_password = "admin123"
attempts = 3
while attempts > 0:
  password = input("Enter password:")
  if password == correct_password:
    print("Access Granted")
    break
  else:
    attempts-= 1
    print("Incorrect password. Attempts left:", attempts)


# while Loop Counter
# # Print numbers from 10 to 1 using while loop. 
i = 10
while i >= 1:
  print(i)
  i-= 1


# break Usage
for i in range(1, 21):
  if i == 13:
    print("Unlucky number found, stopping the loop.")
    break
  print(i)


# continue Usage
for i in range(1,11):
  if i == 5:
    print("Skipping number 5")
    continue
  print(i)


# Server Health Check Simulation
server_loads =[45, 67, 89, 34, 90]
for i in server_loads:
  if i > 80:
    print("CRITICAL:", i)
  else:
    print("NORMAL:", i)


# counting zeros in a list
num = [10, 0, 5, 0, 8, 0]
count = 0
for i in num:
  if i == 0:
    count += 1
print("Number of zeros found", count)