
# 1. Introduction to Python

# Display text on the screen
print("Hello, World!")
print("I am learning Python.")

# Perform mathematical operations
print(10 + 5)
print(20 - 8)
print(6 * 4)
print(15 / 3)

# Display multiple values
print("Python", "Machine Learning")
print("I want to become a software engineer.")
print(100 / 4)
print("Python", "is fun!")


# 3. Variable Naming Rules

# Valid variable names
first_grade = 85
student_name = "Ahmet"
salary_rate = 5000
class_value = 10

print(first_grade)
print(student_name)
print(salary_rate)
print(class_value)

# Python is case-sensitive
age = 21
Age = 25

print(age)
print(Age)


# 4. Python Data Types

# Integer
age = 25
print(type(age))

# Float
height = 1.75
print(type(height))

# Complex
complex_number = 4 + 2j
print(type(complex_number))

# String
name = "Ahmet"
message = "Hello Python!"

print(type(name))
print(name + " " + message)

# Boolean
is_student = True
is_retired = False

print(type(is_student))
print(5 < 3)

# Dynamic typing
value = 10
print(type(value))

value = "Python"
print(type(value))


# 5. String Operations and Slicing

word = "Python"

# String indexing
print(word[0])
print(word[1])

# String slicing
print(word[1:])
print(word[:3])
print(word[1:4])
print(word[1:4:2])

# String length
print(len(word))

# String concatenation
print(word + " programming")


# 6. Type Casting in Python

# Implicit type conversion
number = 10
decimal = 2.5

result = number + decimal
print(result)
print(type(result))

# Float to integer
price = 99.95
whole_price = int(price)
print(whole_price)

# String to integer
text_number = "45"
converted_number = int(text_number)
print(converted_number)

# Decimal string to integer
text_decimal = "42.8"
converted_decimal = int(float(text_decimal))
print(converted_decimal)

# Integer to float
number = 7
print(float(number))

# Integer to string
age = 22
print("My age: " + str(age))

# Boolean conversions
print(bool(0))
print(bool(-15))
print(bool(""))
print(bool(" "))


# 8. Python Operators

# Arithmetic operators
a = 13
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", 2 ** 4)


# Assignment operators
score = 10

score += 5
print("Updated score:", score)

score *= 2
print("Final score:", score)


# Comparison operators
print("Equal:", 5 == 5)
print("Not equal:", 5 != 3)
print("Greater than:", 7 > 10)
print("Less than:", 3 < 5)
print("Greater or equal:", 5 >= 5)
print("Less or equal:", 4 <= 2)


# Logical operators
age = 22
is_student = True

can_get_discount = (age < 25) and is_student

print("Discount available:", can_get_discount)
print("OR example:", age < 18 or is_student)
print("NOT example:", not is_student)


# Even number check
number = 14
is_even = number % 2 == 0

print("Is even:", is_even)


# 9. Print, f-Strings, and User Input

# Basic print function
name = "Mehmet"
print("Hello", name)

# Using the sep parameter
print("2024", "12", "31", sep="-")

# Using the end parameter
print("Loading", end="...")
print("Done!")

# Using f-strings
age = 22
print(f"My name is {name} and I am {age} years old.")

# Number formatting
gpa = 3.45
print(f"Percentage: {gpa / 4 * 100:.1f}%")

# Special characters
print("First line\nSecond line")
print("Name:\tMehmet")

# Getting user input
user_name = input("What is your name? ")

# Converting string input into an integer
user_age = int(input("Enter your age: "))

# Converting string input into a float
height = float(input("Enter your height in meters: "))

# Displaying results
print(f"Hello, {user_name}!")
print(f"In 10 years, you will be {user_age + 10}.")
print(f"Your height is {height * 100:.0f} cm.")


# 10. Python Practice Exercises

# Exercise 1: Welcome Message
first_name = input("First name: ")
last_name = input("Last name: ")

print(f"Welcome, {first_name} {last_name}!")


# Exercise 2: Celsius to Fahrenheit
celsius = float(input("Temperature in Celsius: "))

fahrenheit = celsius * 9 / 5 + 32

print(f"{celsius}°C = {fahrenheit:.1f}°F")


# Exercise 3: Seconds Converter
total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)")


# Exercise 4: Discount Calculator
price = float(input("Product price (TL): "))
discount_percentage = float(input("Discount percentage: "))
quantity = int(input("Quantity: "))

original_total = price * quantity
savings = original_total * discount_percentage / 100
final_payment = original_total - savings

print(f"Final payment: {final_payment:.2f} TL")
print(f"Total savings: {savings:.2f} TL")
