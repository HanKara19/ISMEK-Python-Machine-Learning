
# 1. What Is Python?

Python is a high-level programming language. It is easy to read, write, and learn.

Python supports object-oriented programming and has a large collection of libraries.

## Key Features

### 1. High-Level Language
Python allows developers to write programs without managing many low-level technical details.

### 2. Easy to Read and Learn
Python uses simple and readable syntax, making it suitable for beginners.

### 3. Object-Oriented Programming
Python supports object-oriented programming, which helps organize code using classes and objects.

### 4. Large Library Support
Python provides many libraries for different tasks.

Examples:
- NumPy: Numerical computing
- Pandas: Data analysis
- Matplotlib: Data visualization
- Scikit-learn: Machine learning

## Where Is Python Used?

Python is commonly used in:
- Web development
- Artificial intelligence
- Machine learning
- Data analysis
- Automation

## Summary

Python is a powerful and beginner-friendly programming language. Its simple syntax and large library ecosystem make it useful for many projects.


# 2. Python Variables

A variable is a name that refers to a value in Python.

## Variable Assignment

The `=` operator assigns a value to a variable.

Example:

```python
age = 21
name = "Ahmet"
```

## Updating Variables

Variables can be assigned new values.

```python
number = 10
number = number + 1
print(number)  # 11
```

## Object References

Python variables refer to objects.

Two variables can refer to the same object.

The `id()` function returns an object's identity.

## Shared Lists

```python
a = [1, 2, 3]
b = a

b.append(4)
print(a)  # [1, 2, 3, 4]
```

Both variables refer to the same list.
Changing the list through `b` also affects `a`.


# 3. Python Variable Naming Rules

Python has specific rules for naming variables.

## 1. Variables Cannot Start with Numbers

Incorrect: `1st_grade = 85`

Correct: `first_grade = 85`

Variable names can contain numbers, but they cannot start with a number.

## 2. Variables Cannot Contain Spaces

Incorrect: `student name = "Ahmet"`

Correct: `student_name = "Ahmet"`

Use underscores (`_`) to separate words. This naming style is called snake_case.

## 3. Special Characters Are Not Allowed

Incorrect: `salary-rate = 5000`

Correct: `salary_rate = 5000`

Special characters such as `-`, `*`, and `/` cannot be used in variable names.

## 4. Python Keywords Cannot Be Used

Incorrect: `class = 10`

Correct: `class_value = 10`

Python keywords such as `if`, `for`, `class`, and `def` cannot be used as variable names.

## Best Practices

- Use meaningful variable names.
- Use lowercase letters and underscores.
- Avoid using built-in function names such as `print`.
- Remember that Python is case-sensitive.


## 4. Python Data Types

Every value in Python has a data type. Python automatically determines the type of a value. This is called dynamic typing.

We can use the `type()` function to check the data type of a value.

### 4.1 Numeric Types

Python has three main numeric types:

- `int`: Whole numbers, such as 25 and -10.
- `float`: Decimal numbers, such as 1.75 and 3.14.
- `complex`: Numbers with real and imaginary parts, such as 4 + 2j.

### 4.2 String Type

The `str` type is used to store text.

Strings can be written inside single or double quotation marks.

Example:

```python
name = "Ahmet"
message = 'Hello Python!'
```

### 4.3 Boolean Type

The `bool` type represents two values:

- `True`
- `False`

Boolean values are commonly used in conditions and comparisons.

Example:

```python
is_student = True
is_retired = False

print(5 < 3)  # False
```

### 4.4 Dynamic Typing

Python automatically determines the type of a variable based on its value.

The `type()` function returns the data type of an object.

Example:

```python
age = 25
print(type(age))  # <class 'int'>
```

### Summary

- `int` stores whole numbers.
- `float` stores decimal numbers.
- `complex` stores complex numbers.
- `str` stores text.
- `bool` stores True or False.
- `type()` checks the data type.


## 5. String Operations and Slicing

A string is a sequence of characters.

Python allows us to access, slice, measure, and combine strings.

### 5.1 String Indexing

Indexing allows us to access individual characters.

Python indexing starts at 0.

Example:

```python
word = "Python"

print(word[0])  # P
print(word[1])  # y
```

### 5.2 String Slicing

Slicing allows us to extract parts of a string.

Syntax: `string[start:stop:step]`

- `start`: Starting index.
- `stop`: Ending index (not included).
- `step`: Number of positions to move.

Examples:

```python
word = "Python"

print(word[1:])     # ython
print(word[:3])     # Pyt
print(word[1:4])    # yth
print(word[1:4:2])  # yh
```

### 5.3 String Length

The `len()` function returns the number of characters in a string.

```python
word = "Python"
print(len(word))  # 6
```

### 5.4 String Concatenation

The `+` operator combines strings.

```python
word = "Python"
print(word + " programming")
```

Output: `Python programming`

### Summary

- Indexing accesses individual characters.
- Python indexing starts at 0.
- Slicing extracts parts of a string.
- `len()` returns the string length.
- `+` combines strings.


## 6. Type Casting in Python

Type casting is the process of converting a value from one data type to another.

Python supports two main types of conversion.

### 6.1 Implicit Type Conversion

Python automatically converts some data types during operations.

Example:

```python
number = 10
decimal = 2.5
result = number + decimal

print(result)        # 12.5
print(type(result))  # <class 'float'>
```

### 6.2 Explicit Type Conversion

Programmers can manually convert data types using built-in functions.

#### int() — Convert to Integer

The `int()` function converts a value to an integer.

It removes the decimal part without rounding.

```python
print(int(3.99))  # 3
print(int("45"))  # 45
```

To convert a decimal string to an integer, first use `float()`.

```python
print(int(float("42.8")))  # 42
```

#### float() — Convert to Float

The `float()` function converts numbers and valid numeric strings to floating-point numbers.

```python
print(float(7))       # 7.0
print(float("3.14"))  # 3.14
```

#### str() — Convert to String

The `str()` function converts a value to text.

```python
age = 22
print("My age: " + str(age))
```

#### bool() — Convert to Boolean

The `bool()` function converts values to True or False.

Examples of falsy values:
- `0`
- `0.0`
- `""`
- `None`
- Empty lists and dictionaries

Examples of truthy values:
- Non-zero numbers
- Non-empty strings
- Non-empty lists

```python
print(bool(0))    # False
print(bool(-15))  # True
print(bool(""))   # False
print(bool(" "))  # True
```

### 6.3 Common Type Conversion Errors

Invalid conversions can cause a `ValueError`.

For example, `int("42.8")` cannot directly convert a decimal string into an integer.

Using `int(float("42.8"))` solves this problem.

The `input()` function always returns a string. We often need to convert user input before performing calculations.

### Summary

- Implicit conversion happens automatically.
- Explicit conversion is performed manually.
- `int()` converts values to integers.
- `float()` converts values to decimal numbers.
- `str()` converts values to strings.
- `bool()` converts values to Boolean values.


## 8. Python Operators

Operators are special symbols and keywords used to perform calculations, comparisons, and logical operations.

### 8.1 Arithmetic Operators

Arithmetic operators are used for mathematical operations.

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| + | Addition | 5 + 3 | 8 |
| - | Subtraction | 10 - 4 | 6 |
| * | Multiplication | 3 * 5 | 15 |
| / | Division | 10 / 2 | 5.0 |
| // | Floor Division | 13 // 4 | 3 |
| % | Modulus | 13 % 4 | 1 |
| ** | Exponentiation | 2 ** 3 | 8 |

Example:

```python
a = 13
b = 4

print(a / b)   # 3.25
print(a // b)  # 3
print(a % b)   # 1
print(2 ** 4)  # 16
```

The `/` operator performs normal division.

The `//` operator rounds the division result down.

The `%` operator returns the remainder.

The `**` operator calculates powers.

### 8.2 Assignment Operators

Assignment operators assign or update variable values.

- `=` assigns a value.
- `+=` adds and assigns.
- `-=` subtracts and assigns.
- `*=` multiplies and assigns.

Example:

```python
score = 10

score += 5
print(score)  # 15

score *= 2
print(score)  # 30
```

### 8.3 Comparison Operators

Comparison operators compare values and return True or False.

- `==`: Equal to
- `!=`: Not equal to
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to

Example:

```python
print(5 == 5)  # True
print(5 != 3)  # True
print(7 > 10)  # False
print(3 < 5)   # True
```

### 8.4 Logical Operators

Logical operators combine or modify conditions.

- `and`: Both conditions must be true.
- `or`: At least one condition must be true.
- `not`: Reverses the truth value.

Example:

```python
age = 22
is_student = True

can_get_discount = (age < 25) and is_student

print(can_get_discount)  # True
```

### 8.5 Common Mistakes

- `=` assigns a value, while `==` compares values.
- The `/` operator returns a float.
- The `%` operator returns the remainder.
- Boolean comparisons return True or False.

### Summary

Python operators are used for calculations, value assignments, comparisons, and logical decisions.


## 9. Print, f-Strings, and User Input

Python provides built-in tools for displaying information, formatting text, and receiving user input.

### 9.1 The print() Function

The `print()` function displays information on the screen.

```python
name = "Mehmet"
print("Hello", name)
```

Output: `Hello Mehmet`

#### The sep Parameter

The `sep` parameter changes the separator between values.

```python
print("2024", "12", "31", sep="-")
```

Output: `2024-12-31`

#### The end Parameter

The `end` parameter controls what is printed at the end of a print statement.

```python
print("Loading", end="...")
print("Done!")
```

Output: `Loading...Done!`

### 9.2 f-Strings

An f-string allows us to insert variables and expressions directly into text.

We place the letter `f` before the quotation marks and use curly braces `{}`.

```python
name = "Mehmet"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

#### Number Formatting

f-strings can also format decimal numbers.

```python
gpa = 3.45
print(f"Percentage: {gpa / 4 * 100:.1f}%")
```

Common formatting options:

- `:.1f` displays one decimal place.
- `:.2f` displays two decimal places.
- `:.0f` displays no decimal places.

### 9.3 Special Characters

Special characters control text formatting.

- `\n` creates a new line.
- `\t` inserts a tab.

Example:

```python
print("First line\nSecond line")
```

### 9.4 The input() Function

The `input()` function receives information from the user.

It always returns a string.

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

### 9.5 Converting User Input

We must convert input values before using them in numerical calculations.

```python
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print(f"Age next year: {age + 1}")
print(f"Height in centimeters: {height * 100:.0f}")
```

The `int()` function converts valid integer text into an integer.

The `float()` function converts valid numeric text into a floating-point number.

Invalid numeric input can cause a ValueError.

### Summary

- `print()` displays information.
- `sep` changes the separator between values.
- `end` controls the end of printed output.
- f-strings insert values into text.
- `\n` creates a new line and `\t` inserts a tab.
- `input()` receives information from users.
- `input()` always returns a string.
- `int()` and `float()` convert numeric input.


## 10. Python Practice Exercises

These exercises combine the Python concepts covered in previous sections, including variables, data types, input, type casting, operators, and f-strings.

### Exercise 1: Welcome Message (Easy)

**Task:** Ask the user for their first and last name. Display a welcome message.

Example output:

```text
Welcome, John Smith!
```

**Concepts:**
- The `input()` function receives text.
- Variables store user information.
- f-strings insert values into messages.

### Exercise 2: Celsius to Fahrenheit (Easy)

**Task:** Convert a temperature from Celsius to Fahrenheit.

**Formula:**

F = C * 9 / 5 + 32

Example:

```text
25.0°C = 77.0°F
```

**Concepts:**
- `float()` converts numeric input.
- Arithmetic operators perform calculations.
- `:.1f` displays one decimal place.

### Exercise 3: Seconds Converter (Medium)

**Task:** Convert a given number of seconds into hours, minutes, and seconds.

Example:

```text
3725 seconds = 1 hour, 2 minutes, 5 seconds
```

**Concepts:**
- `//` performs floor division.
- `%` calculates the remainder.
- `int()` converts input into an integer.

**Calculation steps:**

1. Divide the total seconds by 3600 to get hours.
2. Find the remaining seconds using `% 3600`.
3. Divide the remainder by 60 to get minutes.
4. Use `% 60` to get the final seconds.

### Exercise 4: Discount Calculator (Hard)

**Task:** Ask for a product price, discount percentage, and quantity. Calculate the final payment and total savings.

**Formulas:**

Original Total = Price * Quantity

Savings = Original Total * Discount / 100

Final Payment = Original Total - Savings

Example:

```text
Product price: 200
Discount percentage: 20
Quantity: 3

Final payment: 480.00 TL
Total savings: 120.00 TL
```

**Concepts:**
- Input and type conversion
- Arithmetic operators
- Variables
- f-string number formatting

### Summary

These exercises help us practice writing simple Python programs that receive input, perform calculations, and display formatted results.
