
# Python Data Structures

Data structures allow us to store and organize multiple values efficiently.

Python provides four common built-in data structures:

- List
- Tuple
- Set
- Dictionary

## 1. Python Lists

A list is an ordered and mutable collection of items.

Lists are created using square brackets `[]`.

### 1.1 Creating a List

```python
letters = ["a", "b", "c", "d", "e", "a"]
```

A list can contain multiple values, including duplicates.

### 1.2 List Indexing

Indexing allows us to access individual elements.

Python indexing starts at 0.

Negative indexing allows us to access elements from the end.

```python
letters = ["a", "b", "c", "d", "e", "a"]

print(letters[0])   # a
print(letters[2])   # c
print(letters[-1])  # a
```

### 1.3 List Slicing

Slicing extracts a part of a list.

Syntax:

`list[start:stop:step]`

The start index is included, but the stop index is excluded.

```python
letters = ["a", "b", "c", "d", "e", "a"]

print(letters[2:5])
print(letters[:3])
print(letters[::2])
print(letters[::-1])
```

### 1.4 List Concatenation

The `+` operator combines two lists.

```python
letters = ["a", "b", "c"]
letters = letters + ["d"]

print(letters)
```

Output:

```text
['a', 'b', 'c', 'd']
```

A list cannot be directly concatenated with a string using `+`.

### 1.5 List Length

The `len()` function returns the number of elements in a list.

```python
numbers = [10, 20, 30, 40]
print(len(numbers))  # 4
```

### Summary

- Lists store multiple values.
- Lists are ordered and mutable.
- Lists allow duplicate values.
- Indexing starts at 0.
- Negative indexes access elements from the end.
- Slicing extracts parts of a list.
- The `+` operator combines lists.
- `len()` returns the number of elements.


## 2. Python List Methods

List methods allow us to add, remove, search, sort, and modify elements in a list.

Python lists are mutable, meaning their contents can be changed after creation.

### 2.1 append()

The `append()` method adds one element to the end of a list.

```python
fruits = ["apple", "pear"]
fruits.append("banana")

print(fruits)
```

Output: `['apple', 'pear', 'banana']`

### 2.2 insert()

The `insert()` method adds an element at a specified index.

```python
fruits = ["apple", "banana"]
fruits.insert(1, "strawberry")
```

Output: `['apple', 'strawberry', 'banana']`

### 2.3 extend()

The `extend()` method adds all elements from an iterable to the list.

```python
numbers = [1, 2]
numbers.extend([3, 4])

print(numbers)
```

Output: `[1, 2, 3, 4]`

Unlike `append()`, `extend()` adds the elements individually.

### 2.4 remove()

The `remove()` method removes the first matching value from a list.

```python
fruits = ["apple", "pear", "banana"]
fruits.remove("pear")
```

Output: `['apple', 'banana']`

If the value does not exist, Python raises a ValueError.

### 2.5 pop()

The `pop()` method removes and returns an element.

By default, it removes the last element.

```python
numbers = [10, 20, 30]
removed = numbers.pop(1)

print(removed)  # 20
print(numbers)  # [10, 30]
```

### 2.6 sort()

The `sort()` method sorts a list in place.

```python
numbers = [5, 2, 9, 1, 7]

numbers.sort()
print(numbers)
```

Output: `[1, 2, 5, 7, 9]`

For descending order, use `sort(reverse=True)`.

### 2.7 reverse()

The `reverse()` method reverses the current order of the elements.

```python
numbers = [1, 2, 3]
numbers.reverse()
```

Output: `[3, 2, 1]`

### 2.8 index()

The `index()` method returns the index of the first matching value.

```python
numbers = [10, 20, 20, 30]
print(numbers.index(20))  # 1
```

### 2.9 count()

The `count()` method returns the number of occurrences of a value.

```python
numbers = [10, 20, 20, 30]
print(numbers.count(20))  # 2
```

### 2.10 len()

The built-in `len()` function returns the number of elements in a list.

```python
numbers = [10, 20, 30]
print(len(numbers))  # 3
```

### 2.11 Useful Built-in Functions

Python provides additional functions for numerical lists:

- `max()` returns the largest value.
- `min()` returns the smallest value.
- `sum()` calculates the total.
- `len()` counts the elements.

### 2.12 Looping Through a List

A `for` loop can access each element in a list.

The `enumerate()` function provides both the position and the value.

```python
fruits = ["apple", "banana"]

for position, fruit in enumerate(fruits, start=1):
    print(f"{position}. {fruit}")
```

### 2.13 Copying Lists

Assigning a list to another variable does not create a new list.

Both variables refer to the same object.

The `copy()` method creates a new list.

```python
a = [1, 2, 3]
b = a
c = a.copy()

a.append(4)

print(b)  # [1, 2, 3, 4]
print(c)  # [1, 2, 3]
```

The `copy()` method creates a shallow copy. Nested mutable objects may still be shared.

### Summary

- `append()` adds one element.
- `insert()` adds an element at a specific position.
- `extend()` adds multiple elements.
- `remove()` deletes the first matching value.
- `pop()` removes and returns an element.
- `sort()` sorts a list.
- `reverse()` reverses the element order.
- `index()` finds an element's position.
- `count()` counts matching values.
- `copy()` creates a shallow copy.
- `len()` returns the list length.


## 3. Python List Comprehension

List comprehension is a short and readable way to create lists in Python.

It allows us to generate lists using a single line of code.

### 3.1 Traditional For Loop

We can create a list of squared numbers using a for loop.

```python
squares = []

for i in range(1, 11):
    squares.append(i ** 2)

print(squares)
```

### 3.2 Basic List Comprehension

List comprehension performs the same operation in one line.

Syntax:

`[expression for item in iterable]`

Example:

```python
squares = [i ** 2 for i in range(1, 11)]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 3.3 Conditional List Comprehension

We can use an `if` condition to filter elements.

Syntax:

`[expression for item in iterable if condition]`

Example:

```python
even_squares = [
    i ** 2 for i in range(1, 11) if i % 2 == 0
]

print(even_squares)
```

Output:

```text
[4, 16, 36, 64, 100]
```

Only even numbers are included.

### 3.4 List Comprehension with if-else

We can use different expressions based on a condition.

Syntax:

`[value_if_true if condition else value_if_false for item in iterable]`

Example:

```python
numbers = [5, 2, 9, 1, 7]

labels = [
    "even" if n % 2 == 0 else "odd"
    for n in numbers
]

print(labels)
```

Output:

```text
['odd', 'even', 'odd', 'odd', 'odd']
```

### 3.5 Squares for Even Numbers, Cubes for Odd Numbers

We want to process numbers from 1 to 10.

Rules:

- If a number is even, calculate its square.
- If a number is odd, calculate its cube.

```python
results = [
    n ** 2 if n % 2 == 0 else n ** 3
    for n in range(1, 11)
]

print(results)
```

Output:

```text
[1, 4, 27, 16, 125, 36, 343, 64, 729, 100]
```

### Summary

- List comprehension creates lists with less code.
- A for loop can be written inside square brackets.
- An `if` condition filters elements.
- An `if-else` expression applies different operations.
- List comprehension is useful for transforming and filtering data.


## 4. Python Tuples

A tuple is an ordered and immutable collection of elements in Python.

Tuples can store multiple values, including duplicate values.

Unlike lists, tuples cannot be modified after creation.

### 4.1 Creating a Tuple

Tuples are commonly created using parentheses `()`.

```python
letters = ("a", "b", "e", "d", "e", "a")
print(letters)
```

### 4.2 Lists vs Tuples

Lists are mutable, while tuples are immutable.

List example:

```python
numbers = [10, 20, 30]
numbers[0] = 50

print(numbers)  # [50, 20, 30]
```

Tuple example:

```python
numbers = (10, 20, 30)

# This operation raises a TypeError:
# numbers[0] = 50
```

### 4.3 Tuple Indexing and Slicing

Tuples support indexing and slicing.

```python
letters = ("a", "b", "e", "d", "e", "a")

print(letters[0])    # a
print(letters[-1])   # a
print(letters[2:5])  # ('e', 'd', 'e')
```

### 4.4 The index() Method

The `index()` method returns the position of the first matching element.

```python
letters = ("a", "b", "e", "d", "e", "a")

print(letters.index("b"))  # 1
```

### 4.5 The count() Method

The `count()` method returns the number of occurrences of an element.

```python
letters = ("a", "b", "e", "d", "e", "a")

print(letters.count("e"))  # 2
```

### 4.6 Tuple Unpacking

Tuple unpacking allows us to assign tuple elements to separate variables.

```python
location = (41.01, 28.97)

latitude, longitude = location

print(latitude)   # 41.01
print(longitude)  # 28.97
```

### 4.7 When to Use Tuples

Tuples are useful when we want to group values that should not be changed.

Examples include coordinates and fixed configuration values.

### Summary

- Tuples are ordered and immutable.
- Tuples allow duplicate values.
- Tuples support indexing and slicing.
- The `index()` method finds an element's position.
- The `count()` method counts matching elements.
- Tuple unpacking assigns elements to separate variables.


## 5. Python Sets

A set is an unordered collection of unique elements in Python.

Sets do not allow duplicate values.

Sets are useful for removing duplicates and performing mathematical set operations.

### 5.1 Creating a Set

Sets are created using curly braces `{}`.

```python
numbers = {1, 2, 3, 2, 1}
print(numbers)
```

The set contains only three unique elements: 1, 2, and 3.

The order of elements is not guaranteed.

### 5.2 Set Properties

- Sets are unordered.
- Sets do not allow duplicate elements.
- Sets are mutable.
- Sets do not support indexing or slicing.

### 5.3 Union

The union operation combines all unique elements from two sets.

Operator: `|`

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
```

Result: `{1, 2, 3, 4, 5, 6}`

### 5.4 Intersection

The intersection operation returns elements that exist in both sets.

Operator: `&`

```python
print(a & b)
```

Result: `{3, 4}`

### 5.5 Difference

The difference operation returns elements that exist in the first set but not in the second set.

Operator: `-`

```python
print(a - b)
```

Result: `{1, 2}`

The order of the operands matters.

### 5.6 Removing Duplicates

The `set()` function converts an iterable into a set.

It can be used to remove duplicate values from a list.

```python
grades = [70, 85, 70, 90, 85]

unique_grades = set(grades)
print(unique_grades)
```

The result contains the unique values 70, 85, and 90.

We can also convert the set back into a list:

```python
unique_list = list(set(grades))
```

The original element order is not guaranteed.

### 5.7 Adding Elements

The `add()` method adds an element to a set.

```python
club = {"Ali", "Veli", "Ayse"}
club.add("Can")
```

### 5.8 Removing Elements

The `discard()` method removes an element if it exists.

It does not raise an error if the element is missing.

```python
club.discard("Veli")
```

### 5.9 Membership Testing

The `in` operator checks whether an element exists in a set.

```python
print("Ali" in club)  # True
```

### Summary

- Sets contain unique elements.
- Sets are unordered and mutable.
- `|` performs union.
- `&` performs intersection.
- `-` performs difference.
- `set()` converts an iterable to a set.
- `add()` adds an element.
- `discard()` removes an element if present.
- `in` checks membership.


## 6. Python Dictionaries

A dictionary is a collection of key-value pairs in Python.

Dictionaries allow us to store and access information using keys instead of numeric indexes.

They are created using curly braces `{}`.

### 6.1 Creating a Dictionary

```python
student = {
    "name": "Zeynep",
    "age": 21,
    "department": "Software Engineering"
}
```

Each key is connected to a value.

Keys must be unique within a dictionary.

### 6.2 Accessing Values

We can access a value using its key.

```python
print(student["name"])  # Zeynep
print(student["age"])   # 21
```

Accessing a missing key with square brackets raises a KeyError.

### 6.3 The get() Method

The `get()` method retrieves a value without raising a KeyError if the key is missing.

```python
print(student.get("phone"))             # None
print(student.get("phone", "Unknown"))  # Unknown
```

We can provide a default value as the second argument.

### 6.4 Dictionary Methods

#### keys()

Returns a view containing all dictionary keys.

```python
print(list(student.keys()))
```

#### values()

Returns a view containing all dictionary values.

```python
print(list(student.values()))
```

#### items()

Returns a view containing key-value pairs.

```python
print(list(student.items()))
```

### 6.5 Updating and Adding Values

We can update an existing value or add a new key.

```python
student["age"] = 22
student["city"] = "Istanbul"
```

The `update()` method can update multiple values.

```python
student.update({
    "age": 23,
    "city": "Ankara"
})
```

### 6.6 Removing Elements

The `pop()` method removes a key and returns its value.

```python
student.pop("city")
```

The `del` statement can also remove a key.

```python
del student["department"]
```

### 6.7 Nested Dictionaries

A nested dictionary is a dictionary inside another dictionary.

```python
person = {
    "name": "Sevval",
    "location": {
        "birth_city": "Istanbul",
        "current_city": "Berlin"
    }
}

print(person["location"]["current_city"])
```

Output: `Berlin`

### 6.8 Looping Through a Dictionary

The `items()` method allows us to access keys and values in a loop.

```python
student = {"name": "Elif", "age": 21}

for key, value in student.items():
    print(f"{key}: {value}")
```

### 6.9 Dictionary Membership

The `in` operator checks whether a key exists.

```python
print("name" in student)   # True
print("phone" in student)  # False
```

### 6.10 List of Dictionaries

We can store multiple dictionaries inside a list.

This is useful for working with structured data.

```python
students = [
    {"name": "Ali", "grade": 80},
    {"name": "Ayse", "grade": 95}
]

for student in students:
    print(student["name"], student["grade"])
```

### Summary

- Dictionaries store key-value pairs.
- Keys are used to access values.
- `get()` safely retrieves values.
- `keys()` returns dictionary keys.
- `values()` returns dictionary values.
- `items()` returns key-value pairs.
- `update()` updates dictionary values.
- `pop()` removes a key and returns its value.
- Dictionaries can contain other dictionaries.
- Dictionaries can be used with for loops.


## 7. Python Practice Exercises

These exercises help us practice Python data structures, loops, conditions, and basic data processing.

### Exercise 1: Maximum, Minimum, and Average

**Difficulty:** Easy

**Task:** Find the maximum, minimum, and average values in a list without using `max()` or `min()`.

Example list:

```python
numbers = [12, 45, 7, 23, 56, 89, 3]
```

Expected results:

- Maximum: 89
- Minimum: 3
- Average: 33.57

**Concepts Used:**

- Lists
- For loops
- If conditions
- Comparison operators
- The `len()` function

**Explanation:**

We start by assigning the first element to both the largest and smallest variables.

We then use a for loop to compare every number and update these variables.

We also calculate the sum of all numbers and divide it by the number of elements to find the average.

### Exercise 2: Remove Duplicates and Sort

**Difficulty:** Easy to Medium

**Task:** Ask the user to enter comma-separated numbers. Remove duplicates and display the remaining numbers in ascending order.

Example input:

```text
5,3,8,5,2,3
```

Expected output:

```text
[2, 3, 5, 8]
```

**Concepts Used:**

- User input
- String splitting
- List comprehension
- Type conversion
- Sets
- Sorting

**Explanation:**

1. `input()` receives the numbers as a string.
2. `split(",")` separates the numbers.
3. `int()` converts each value into an integer.
4. `set()` removes duplicate values.
5. `sorted()` sorts the unique numbers.

### Exercise 3: Word Frequency Counter

**Difficulty:** Medium

**Task:** Ask the user to enter a sentence and count how many times each word appears.

Example input:

```text
Python is fun Python is easy
```

Expected output:

```text
python: 2
is: 2
fun: 1
easy: 1
```

**Concepts Used:**

- Strings
- Dictionaries
- For loops
- The `lower()` method
- The `split()` method
- The `get()` method

**Explanation:**

The program converts the sentence to lowercase and splits it into words.

A dictionary stores each word as a key and its frequency as a value.

The expression `frequency.get(word, 0) + 1` increases the word count.

This basic version does not separately remove punctuation.

### Exercise 4: Student Grade Analyzer

**Difficulty:** Hard

**Task:** Store student grades in a dictionary, calculate each student's average grade, and find the student with the highest average.

Example:

```python
grades = {
    "Ali": [80, 90],
    "Ayse": [95, 100, 85]
}
```

Expected output:

```text
Ali: 85.0
Ayse: 93.3
Best student: Ayse
```

**Concepts Used:**

- Dictionaries
- Lists
- For loops
- The `sum()` function
- The `len()` function
- The `max()` function
- f-string formatting

**Explanation:**

The program loops through each student and calculates their average grade.

It stores the results in a new dictionary.

The expression `max(averages, key=averages.get)` finds the student with the highest average.

### Summary

These exercises demonstrate how Python data structures can solve practical problems.

We practiced finding numerical values, removing duplicates, counting words, and analyzing student grades.

