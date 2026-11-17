
# 1. Python Lists

# Creating a list
letters = ["a", "b", "c", "d", "e", "a"]
print("Original list:", letters)

# Accessing list elements
print("First element:", letters[0])
print("Third element:", letters[2])
print("Last element:", letters[-1])

# List slicing
print("Slice [2:5]:", letters[2:5])
print("First three:", letters[:3])
print("Every second:", letters[::2])
print("Reversed list:", letters[::-1])

# List concatenation
letters = letters + ["f"]
print("Updated list:", letters)

# List length
print("Number of elements:", len(letters))

# A list can store different data types
student = ["Alex", 22, 3.5, True]
print("Student information:", student)


# 2. Python List Methods

# append()
fruits = ["apple", "pear", "banana"]
fruits.append("cherry")
print("Append:", fruits)

# insert()
fruits.insert(1, "strawberry")
print("Insert:", fruits)

# extend()
fruits.extend(["orange", "grape"])
print("Extend:", fruits)

# remove()
fruits.remove("pear")
print("Remove:", fruits)

# pop() with an index
removed_fruit = fruits.pop(2)
print("Removed fruit:", removed_fruit)
print("After pop:", fruits)

# pop() without an index
last_fruit = fruits.pop()
print("Last removed fruit:", last_fruit)

# sort()
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print("Sorted:", numbers)

# reverse()
numbers.reverse()
print("Reversed:", numbers)

# index()
values = [10, 20, 20, 30]
print("Index of 20:", values.index(20))

# count()
print("Count of 20:", values.count(20))

# len()
print("List length:", len(values))

# Built-in numerical functions
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# Loop through list elements
for fruit in fruits:
    print(fruit.upper())

# enumerate()
for position, fruit in enumerate(fruits, start=1):
    print(f"{position}. {fruit}")

# Reference assignment vs shallow copy
a = [1, 2, 3]
b = a
c = a.copy()

a.append(4)

print("Original list:", a)
print("Shared reference:", b)
print("Copied list:", c)


# 3. Python List Comprehension

# Traditional for loop
squares_traditional = []

for i in range(1, 11):
    squares_traditional.append(i ** 2)

print("Traditional squares:", squares_traditional)


# Basic list comprehension
squares = [i ** 2 for i in range(1, 11)]

print("Squares:", squares)


# Conditional list comprehension
even_squares = [
    i ** 2 for i in range(1, 11) if i % 2 == 0
]

print("Even squares:", even_squares)


# List comprehension with if-else
numbers = [5, 2, 9, 1, 7]

labels = [
    "even" if n % 2 == 0 else "odd"
    for n in numbers
]

print("Number labels:", labels)


# Squares for even numbers, cubes for odd numbers
results = [
    n ** 2 if n % 2 == 0 else n ** 3
    for n in range(1, 11)
]

print("Original numbers:", list(range(1, 11)))
print("Processed numbers:", results)


# 4. Python Tuples

# Creating a list and a tuple
letters_list = ["a", "b", "e", "d", "e", "a"]
letters_tuple = ("a", "b", "e", "d", "e", "a")

print("List:", letters_list)
print("Tuple:", letters_tuple)

# Modifying a list
letters_list[0] = 12312
print("Modified list:", letters_list)

# Tuples are immutable
# The following operation raises a TypeError:
# letters_tuple[0] = 12312

# Tuple indexing
print("First element:", letters_tuple[0])
print("Last element:", letters_tuple[-1])

# Tuple slicing
print("Tuple slice:", letters_tuple[2:5])

# Tuple methods
print("Index of b:", letters_tuple.index("b"))
print("Count of e:", letters_tuple.count("e"))

# Tuple unpacking
location = (41.01, 28.97)

latitude, longitude = location

print("Latitude:", latitude)
print("Longitude:", longitude)

# Checking the data type
print("Data type:", type(location))


# 5. Python Sets

# Creating a set
numbers = {1, 2, 3, 2, 1}

print("Unique numbers:", numbers)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference A - B:", a - b)
print("Difference B - A:", b - a)

# Removing duplicates from a list
grades = [70, 85, 70, 90, 85]

unique_grades = set(grades)
print("Unique grades:", unique_grades)

# Converting a set back to a list
unique_list = list(set(grades))
print("Unique list:", unique_list)

# Club membership example
club_a = {"Ali", "Veli", "Ayse"}
club_b = {"Ayse", "Fatma"}

print("All members:", club_a | club_b)
print("Common members:", club_a & club_b)
print("Only club A:", club_a - club_b)

# Adding an element
club_a.add("Can")
print("After adding:", club_a)

# Removing an element safely
club_a.discard("Zeynep")

# Checking membership
print("Is Ali in club A?", "Ali" in club_a)
print("Is Fatma in club A?", "Fatma" in club_a)


# 6. Python Dictionaries

# Creating a dictionary
student = {
    "name": "Zeynep",
    "age": 21,
    "department": "Software Engineering"
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])
print("Data type:", type(student))

# Using the get() method
print("Phone:", student.get("phone"))
print("Phone:", student.get("phone", "Unknown"))

# Dictionary methods
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# Updating an existing value
student["age"] = 22

# Adding a new key
student["city"] = "Istanbul"

print("Updated student:", student)

# Updating multiple values
student.update({
    "age": 23,
    "city": "Ankara"
})

print("After update:", student)

# Removing a key
removed_city = student.pop("city")
print("Removed city:", removed_city)

# Deleting a key
del student["department"]

print("After deletion:", student)

# Nested dictionary
person = {
    "name": "Sevval",
    "age": 23,
    "location": {
        "birth_city": "Istanbul",
        "current_city": "Berlin"
    }
}

print("Current city:", person["location"]["current_city"])

# Accessing nested values with get()
print(
    "Birth city:",
    person.get("location", {}).get("birth_city")
)

# Looping through a dictionary
student = {
    "name": "Elif",
    "age": 21,
    "department": "Computer Engineering"
}

for key, value in student.items():
    print(f"{key}: {value}")

# Checking dictionary membership
print("Has name:", "name" in student)
print("Has phone:", "phone" in student)

# List of dictionaries
students = [
    {"name": "Ali", "grade": 80},
    {"name": "Ayse", "grade": 95}
]

for student in students:
    print(student["name"], student["grade"])


# 7. Python Practice Exercises

# Exercise 1: Maximum, Minimum, and Average

numbers = [12, 45, 7, 23, 56, 89, 3]

largest = numbers[0]
smallest = numbers[0]
total = 0

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

    total += number

average = total / len(numbers)

print("Maximum:", largest)
print("Minimum:", smallest)
print(f"Average: {average:.2f}")


# Exercise 2: Remove Duplicates and Sort

user_input = input("Enter comma-separated numbers: ")

numbers = [
    int(item) for item in user_input.split(",")
]

unique_numbers = sorted(set(numbers))

print("Unique sorted numbers:", unique_numbers)


# Exercise 3: Word Frequency Counter

sentence = input("Enter a sentence: ").lower()

frequency = {}

for word in sentence.split():
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequencies:")

for word, count in frequency.items():
    print(f"{word}: {count}")


# Exercise 4: Student Grade Analyzer

grades = {
    "Ali": [80, 90],
    "Ayse": [95, 100, 85]
}

averages = {}

for name, grade_list in grades.items():
    averages[name] = sum(grade_list) / len(grade_list)
    print(f"{name}: {averages[name]:.1f}")

best_student = max(averages, key=averages.get)

print(f"Best student: {best_student}")
