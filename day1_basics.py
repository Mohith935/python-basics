print("hello world")
print("welcome back!")

name = "shiva"
age = 25
is_engineer = True
print(name)
print(age)
print(is_engineer)

print(type(name))
print(type(age))
print(type(is_engineer))


# Taking User Input
user_name = input("Enter your name:")
user_age = input("Enter your age:")
user_city = input("Enter your city:")
# Note: input() gives string by default.
print(type(user_age))
print("Hello, " + user_name + " You are " + user_age + " years old and lives in " + user_city)


# Basic Arithmetic Operations
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print("addition:", num1 + num2)
print("subtraction:", num1 - num2)
print("multiplication:", num1 * num2)
print("division:", num1 / num2)
print("modulus:", num1 % num2)


# Area Calculator
radius = float(input("Enter radius of circle:"))
area = 3.14 * radius * radius
print("Area of circle:", area)


# swap two numbers without using third variable
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
print("Before swapping: x =", x, "y =", y) 
x = x + y
y = x - y
x = x - y
print("After swapping: x =", x, "y =", y)