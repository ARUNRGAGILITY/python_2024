###########################################################
'''
In this part 

we will see 
Python Data-Types like List, Tuple, Set, Dictionary
Python Operators

'''

###########################################################
# Python Data types

# List, Tuple, Set, Dictionary

# -------------------------------------------------------- #
# List
'''
A Python list is a versatile data structure which 
can hold an ordered sequence of elements. 
These elements can be of any type, 
including integers, strings, or even other lists. 
Lists are mutable, meaning they can be modified after creation. 
They are defined by enclosing elements in square brackets [], 
and elements within a list are accessed by their index, 
with indexing starting at 0 for the first element.
'''

## List Examples ##

# Creating a list
my_list = [1, 2, 3, 'Python', 'Language']

# Accessing elements
first_element = my_list[0]  # Access the first element (1)
last_element = my_list[-1]  # Access the last element ('Django')

# Modifying elements
my_list[1] = 'changed'  # Change the second element

# Adding elements
my_list.append('new item')  # Add a new item to the end of the list

# Removing elements
my_list.remove('Python')  # Remove the first occurrence of 'Python'

# Looping through a list
for item in my_list:
    print(item)

## Slicing a List ##
my_list = [0, 1, 2, 3, 4, 5]
slice_list = my_list[1:4]  # Returns [1, 2, 3]

## Concatenation ##
list_one = [1, 2, 3]
list_two = [4, 5, 6]
combined_list = list_one + list_two  # Returns [1, 2, 3, 4, 5, 6]

## Replication ##
my_list = [1, 2, 3]
repeated_list = my_list * 3  # Returns [1, 2, 3, 1, 2, 3, 1, 2, 3]

## Length of a List ##
my_list = [1, 2, 3]
length = len(my_list)  # Returns 3

## Sorting of a List #
my_list = [3, 1, 4, 1, 5]
my_list.sort()  # The list becomes [1, 1, 3, 4, 5]

## Reversing ##
my_list = [1, 2, 3]
my_list.reverse()  # The list becomes [3, 2, 1]

## Indexing ##
my_list = ['a', 'b', 'c', 'b']
index = my_list.index('b')  # Returns 1

## Counting ##
my_list = [1, 2, 3, 2, 2, 4]
count = my_list.count(2)  # Returns 3

## Inserting items in a  List ##
my_list = [1, 2, 4]
my_list.insert(2, 3)  # The list becomes [1, 2, 3, 4]

## Popping from a List ##
my_list = [1, 2, 3]
popped_item = my_list.pop(1)  # Removes and returns '2', list becomes [1, 3]

## Clearing a List ##
my_list = [1, 2, 3]
my_list.clear()  # The list becomes []

## Copying a List ##
my_list = [1, 2, 3]
copied_list = my_list.copy()  # copied_list is a new list with the same items

## Extending a list with another list ##
# Original list
my_list = [1, 2, 3]
# Another list
another_list = [4, 5, 6]
# Using extend to add elements of another_list to my_list
my_list.extend(another_list)
# Now my_list becomes [1, 2, 3, 4, 5, 6]
print(my_list)

## Unpacking a list into variables ##
# A list with three elements
my_list = [1, 2, 3]

# Unpacking the list into variables
a, b, c = my_list

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

## Nested Lists ##
# A nested list, representing a 2x3 matrix
nested_list = [[1, 2, 3], [4, 5, 6]]

# Accessing elements
print(nested_list[0])  # Output: [1, 2, 3]
print(nested_list[1][2])  # Output: 6 (third element of the second list)

# Iterating over a nested list
for inner_list in nested_list:
    for item in inner_list:
        print(item, end=' ')  # Output: 1 2 3 4 5 6
    print()


## List Comprehensions ##
'''
A concise way to create lists with conditionals and nested loops
'''
squared_numbers = [x**2 for x in range(10) if x % 2 == 0]

## List sorting with custom key ##
fruits = ["apple", "banana", "cherry"]
fruits.sort(key=len)  # Sort by length of the fruit name

## Flattening a List ##
'''
Converta a multi-dimensional list 
into a
single list
'''
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]


## Practical Examples for List Usage
'''
Example1: Data Aggregation and Analysis (simple one)
'''

# List of temperatures for each day of the week
temperatures = [29, 31, 30, 32, 33, 31, 30]

# Calculating the average temperature
average_temperature = sum(temperatures) / len(temperatures)

print("Average Temperature for the Week:", average_temperature)

'''
Example2: TextEditor undo option (using like Stack)
'''
class TextEditor:
    def __init__(self):
        self.content = ""
        self.history = []

    def type(self, text):
        self.history.append(self.content)
        self.content += text

    def undo(self):
        if self.history:
            self.content = self.history.pop()
        else:
            print("No more actions to undo.")

# Usage
editor = TextEditor()
editor.type("Hello")
editor.type(" World")
print("Current Content:", editor.content)  # Hello World
editor.undo()
print("After Undo:", editor.content)  # Hello

'''
Example3: Batch Processing and Automation
'''
def send_message(recipient, message):
    print(f"Sending message to {recipient}: '{message}'")

# List of recipients
recipients = ["user1@example.com", "user2@example.com", "user3@example.com"]

# Message to be sent
message = "Hello! This is an automated notification."

# Sending the message to all recipients
for recipient in recipients:
    send_message(recipient, message)


'''
Example4: Course Registration System
'''
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []  # List to store enrolled students

    def enroll_student(self, student_name):
        self.students.append(student_name)

    def unenroll_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
        else:
            print(f"Student {student_name} is not enrolled in {self.name}.")

    def display_students(self):
        print(f"Students enrolled in {self.name}:")
        for student in self.students:
            print(student)

# Usage
math_course = Course("Mathematics")
math_course.enroll_student("Anand")
math_course.enroll_student("Bharath")
math_course.enroll_student("Charlie")
math_course.enroll_student("Vikram")
math_course.enroll_student("Sonia")

math_course.display_students()  # Displays students in Mathematics
math_course.unenroll_student("Vikram")  # Unenroll Vikram
math_course.display_students()  # Displays updated student list



#######################################################
# Tuple

'''
A tuple in Python is a fundamental data structure that 
is similar to a list, but with a key difference: 
tuples are immutable. This means that once a tuple is created, 
its contents cannot be changed, added to, or removed. 
Tuples are commonly used for data that shouldn't be modified 
and can serve as a safe way to represent fixed collections of items.
Tuples are defined by enclosing elements in parentheses ():
'''

## Tuples Examples

# Creating a tuple
my_tuple = (1, "Hello", 3.14)

# Creating a tuple with single element, ',' is necessary
single_tuple = (1,)  # Without the comma, it's just a number within parentheses


# Accessing elements
first_element = my_tuple[0]  # Access the first element (1)

# Tuples are immutable, so elements cannot be changed
# my_tuple[1] = "World"  # This would raise an error

# Length of a tuple
length = len(my_tuple)  # Returns 3

# Looping through a tuple
for item in my_tuple:
    print(item)

## Accessing tuple via negative indexing
last_element = my_tuple[-1]  # Last element
print(last_element)  # Output: 'Python'

## Slicing a tuple ##
sliced_tuple = my_tuple[1:3]  # Elements from index 1 to 2
print(sliced_tuple)  # Output: (2, 3)

## Concatenation in Tuples ##
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

## Repetition ##
repeated_tuple = tuple1 * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)

## Getting the Length of a tuple ##
my_tuple = (1, "Hello", 3.14)
length = len(my_tuple)
print(length)  # Output: 3

## Membership testing in tuple ##
my_tuple = (3, 4, 2, 2, 2, 5, 5, 6)
exists = 2 in my_tuple
print(exists)  # Output: True

## Count of the elements in the tuple ##
my_tuple = (3, 4, 2, 2, 2, 2, 2,  5, 5, 6)
count = my_tuple.count(2)
print(count)  # Output: 2

## Index of the tuple ##
my_tuple = (1, 4, 6, 5, 'Python', 'language')
index = my_tuple.index('Python')
print(index)  # Output: 3

## Unpacking with tuples ##
t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # Output: 1 2 3

## Nested tuples ##
nested_tuple = (1, (2, 3), 4)
print(nested_tuple)  # Output: (1, (2, 3), 4)


## ** tuple advanced topics: refer to collections ##
'''
Part of the collections module, named tuples allow you to create tuples with named fields
'''
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

## Tuple packing, unpacking, swapping ##
a, b = 1, 2
a, b = b, a  # Swapping values

## Tuple assignments in Loops ##
for a, b in [(1, 2), (3, 4), (5, 6)]:
    print(a, b)

## Python Set examples ##

'''
Example1: Returning multiple values
Tuples are commonly used for grouping multiple values 
to pass into or return from a function.

In this example, the min_max function returns a tuple 
containing the minimum and maximum values from a list of numbers.
'''
def min_max(numbers):
    return min(numbers), max(numbers)

# Usage
result = min_max([1, 2, 3, 4, 5])
print(result)  # Output: (1, 5)

'''
Example2: Use Tuples where the data should not be changed
'''
dimensions = (1920, 1080)  # Screen resolution

# Trying to change an element will raise an error
# dimensions[0] = 1024  # Uncommenting this line would raise an error

'''
Example3: Returning Multiple values (again one example)
The get_user function returns both the name and age of a 
user as a tuple, which can be unpacked into separate variables.
'''
def get_user():
    # Simulate fetching user data
    name = "Alice"
    age = 30
    return name, age  # Returning a tuple

# Usage
user_name, user_age = get_user()
print(user_name, user_age)  # Output: Alice 30

'''
Example4: Complex Data Structures with tuples
Here, the student tuple contains a string, a list, and another tuple.
'''
student = ("John Doe", ["Math", "Science"], (1995, 4, 12))

name, subjects, dob = student
print(name)        # Output: John Doe
print(subjects)    # Output: ['Math', 'Science']
print(dob)         # Output: (1995, 4, 12)

'''
Example5: Named tuple
positional or keyword arguments also in this example
The Point1 takes 11 as default for x as positional and y with keyword argument
The Point2 takes 40 for  x and 50 for y through keyword
'''
from collections import namedtuple

Point1 = namedtuple('Point1', ['x', 'y'])
p = Point1(11, y=22)

print(p.x, p.y)  # Output: 11 22

Point2 = namedtuple('Point2', ['x', 'y'])
p = Point2(x=40, y=50)

print(p.x, p.y)  # Output: 40,50


############################################################

# Python Set
'''
A set in Python is a collection data type that is 
unordered, mutable, and iterable. The most notable 
characteristic of a set is that it is composed of 2
unique elements: it does not allow duplicate values. 
This makes sets particularly useful for operations 
involving uniqueness and for performing mathematical 
set operations like unions, intersections, differences, 
and symmetric differences.

Mathematical Set Operations:
 Sets support operations like union (|), intersection (&), 
 difference (-), and symmetric difference (^).
'''


## Creating a Set ##
# Creating a set with curly braces
my_set = {1, 2, 3, 4, 5}

# Creating a set from a list using set()
my_other_set = set([3, 4, 5, 6, 7])

# Sets automatically remove duplicates
my_set_with_duplicates = {1, 2, 2, 3, 4}
print(my_set_with_duplicates)  # Output: {1, 2, 3, 4}

# Adding an element
my_set.add(6)  # {1, 2, 3, 4, 5, 6}

# Removing an element
my_set.remove(6)  # Raises a KeyError if the element is not found

# Discarding an element (does not raise an error if the element is not found)
my_set.discard(5)  # {1, 2, 3, 4}

# Checking if an element is in a set
print(2 in my_set)  # Output: True

# Pop an element from a set / removed #
element = my_set.pop()
# element is a removed item from my_set

# Remove all the elements / clear the set #
my_set.clear()
# my_set is now an empty set {}

# Check Subset
a = {1, 2}
b = {1, 2, 3}
is_subset = a.issubset(b)
# is_subset is True

# Check Superset
is_superset = b.issuperset(a)
# is_superset is True

# Check disjoint 
c = {4, 5}
is_disjoint = a.isdisjoint(c)
# is_disjoint is True as a and c have no common elements

# Set copy 
my_set_copy = my_set.copy()

# Set comprehensions 
squared_set = {x**2 for x in range(5)}
# squared_set is {0, 1, 4, 9, 16}

# Frozen Set or Immutable Set
immutable_set = frozenset(['apple', 'banana'])
# immutable_set.add('cherry')  # This would raise an AttributeError

'''
Union (|): The union of my_set and my_other_set combines 
all elements from both sets, without duplicates. 
The result is {1, 2, 3, 4, 5, 6, 7}.

Intersection (&): The intersection of my_set and my_other_set 
includes only the elements that are present in both sets. 
The result is {3, 4, 5}.

Difference (-): The difference between my_set and my_other_set 
consists of elements that are in my_set but not in my_other_set. 
The result is {1, 2}.

Symmetric Difference (^): The symmetric difference between 
my_set and my_other_set includes elements that are in 
either of the sets but not in their intersection. 
The result is {1, 2, 6, 7}. ​

'''
# Union, Intersection, Difference, and Symmetric Difference
union_set = my_set | my_other_set
intersection_set = my_set & my_other_set
difference_set = my_set - my_other_set
symmetric_difference_set = my_set ^ my_other_set

# Defining the sets
my_set = {1, 2, 3, 4, 5}
my_other_set = {3, 4, 5, 6, 7}

# Union: Combines all elements from both sets, removing duplicates
union_set = my_set | my_other_set
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

# Intersection: Elements that are common in both sets
intersection_set = my_set & my_other_set
print("Intersection:", intersection_set)  # Output: {3, 4, 5}

# Difference: Elements in my_set but not in my_other_set
difference_set = my_set - my_other_set
print("Difference:", difference_set)  # Output: {1, 2}

# Symmetric Difference: Elements in either set, but not in both
symmetric_difference_set = my_set ^ my_other_set
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 6, 7}


# Python Set Examples
'''
Example1: Removing Duplicates
'''
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

'''
Example2: Membership testing
'''
allowed_users = {'Alice', 'Bob', 'Charlie'}
user = 'Daisy'

if user in allowed_users:
    print(f"{user} is allowed.")
else:
    print(f"{user} is not allowed.")

'''
Example3: Set Operations
'''
# Two sets of items
set_a = {'apple', 'banana', 'cherry'}
set_b = {'cherry', 'dragonfruit', 'apple'}

# Finding common items (intersection)
common = set_a & set_b
print("Common items:", common)

# Finding unique items (symmetric difference)
unique = set_a ^ set_b
print("Unique items:", unique)


'''
Example4: Deduplication in data processing
'''
data = ["data1", "data2", "data1", "data3", "data2"]
processed_data = set(data)

for datum in processed_data:
    print(f"Processing {datum}")
    
    
############################################################
# Python Dictionary 
'''
A dictionary in Python is a collection data type that is 
unordered, mutable, and indexed. Dictionaries store data 
as key-value pairs, making them a highly efficient way 
to organize and access data. They are one of the most 
commonly used data structures in Python, particularly 
because of their flexibility and performance characteristics.

Key-Value Pairs: Each element in a dictionary is a key-value pair. 
The key is used to index the value. Keys in a dictionary must be 
unique and immutable (like strings, numbers, or tuples).

Mutable: You can add, modify, and remove key-value pairs in a dictionary.

Dynamic: Dictionaries can grow or shrink in size as needed.

Unordered: Dictionaries in Python 3.7 and later are ordered 
collections, but it's best to think of them as unordered. 
The order of insertion is preserved, but you shouldn't rely on it in most cases.

Flexible Data Types: Both the keys and values in a dictionary can be of any data type.

Efficient Lookup: Accessing a value through its key is very fast,
regardless of the size of the dictionary.
'''

# Dictionary
# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}

# Creating a dictionary in two ways
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# or
my_dict = dict(name="Alice", age=25, city="New York", is_student=True)


# Accessing elements
print(my_dict["name"])  # Output: Alice

# Adding a new key-value pair
my_dict["city"] = "New York"

# Modifying an existing key-value pair
my_dict["age"] = 26

# Removing a key-value pair
del my_dict["is_student"]

# Checking if a key exists
if "city" in my_dict:
    print("City is present")

# Iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")



# Iterating the dictionary with three main options
# by dictionary.items() => getting key, value pair
# by dictionary.keys() => getting the key and the reading value
# by dictionary.values() => getting the values

for key, value in my_dict.items():
    print(key, value)

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

# Dictonary Comprehension
squared_dict = {x: x*x for x in range(6)}
print(squared_dict)


# Merging dictionaries
other_dict = {"country": "USA", "city": "Boston"}
my_dict.update(other_dict)
# or
merged_dict = {**my_dict, **other_dict}

# Copying a Dictionary
my_dict_copy = my_dict.copy()
# or
my_dict_copy = dict(my_dict)

# Nested dictionary
nested_dict = {"child1": {"name": "Bob", "age": 5}, "child2": {"name": "Alice", "age": 7}}

# Safely reading values
email = my_dict.get("email", "Not provided")
print(email)


# Python Dictionary examples

'''
Example1: Accessing with unique key concept
'''
# Storing user information
users = {
    "user1": {"name": "Alice", "age": 25, "email": "alice@example.com"},
    "user2": {"name": "Bob", "age": 30, "email": "bob@example.com"}
}

# Accessing data
print(users["user1"]["name"])  # Output: Alice

'''
Example2: Configuration Settings
'''
config = {
    "path": "/usr/bin/",
    "max_retries": 5,
    "debug_mode": False
}

# Accessing configuration
max_retries = config["max_retries"]

'''
Example3: Counting the items 
'''
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}

'''
Example4: Dictionary as cache for extensive computations
The provided factorial function is an example of memoization 
using a dictionary (cache). Memoization is an optimization 
technique used primarily to speed up computer programs by 
storing the results of expensive function calls and returning 
the cached result when the same inputs occur again.
'''
def factorial(n, cache={}):
    if n in cache:
        return cache[n]
    if n == 1:
        return 1
    else:
        cache[n] = n * factorial(n-1, cache)
        return cache[n]

print(factorial(5))  # Output: 120

'''
Example5: Representing a Graph
'''
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# Accessing neighbors of a node
neighbors = graph["A"]

'''
Example6: Dictionary to JSON data interchange (Javascript Object Notation)
'''
import json

json_data = '{"name": "Alice", "age": 25, "city": "New York"}'
data = json.loads(json_data)  # Convert JSON to a dictionary

new_json_data = json.dumps(data)  # Convert dictionary back to JSON

'''
Example7: Multi-Dimensional Data
'''
# Storing data in a 2D grid format
grid = {
    (0, 0): "grass",
    (0, 1): "sand",
    (1, 0): "water",
    (1, 1): "rock"
}

terrain = grid[(1, 0)]  # Accessing the terrain at position (1, 0)



# -------------------------------------------------------- #
# There are 8 types of Python Operators

'''
1. Arithmetic Operators
Arithmetic operators are used to perform mathematical 
operations like addition, subtraction, multiplication, etc.

+: Addition (e.g., a + b)
-: Subtraction (e.g., a - b)
*: Multiplication (e.g., a * b)
/: Division (e.g., a / b)
%: Modulus (e.g., a % b returns the remainder of division)
**: Exponentiation (e.g., a ** b is a raised to the power of b)
//: Floor division (e.g., a // b performs division and rounds down to the nearest integer)
'''
# Addition
print(5 + 3)  # Output: 8

# Subtraction
print(5 - 3)  # Output: 2

# Multiplication
print(5 * 3)  # Output: 15

# Division
print(5 / 2)  # Output: 2.5

# Modulus (remainder)
print(5 % 2)  # Output: 1

# Exponentiation
print(2 ** 3)  # Output: 8

# Floor Division
print(5 // 2)  # Output: 2

'''
2. Comparison (Relational) Operators
Comparison operators compare values and return True or False 
based on the validity of the condition.

==: Equal to (e.g., a == b)
!=: Not equal to (e.g., a != b)
>: Greater than (e.g., a > b)
<: Less than (e.g., a < b)
>=: Greater than or equal to (e.g., a >= b)
<=: Less than or equal to (e.g., a <= b)

'''
a, b = 5, 3

# Equal to
print(a == b)  # Output: False

# Not equal to
print(a != b)  # Output: True

# Greater than
print(a > b)  # Output: True

# Less than
print(a < b)  # Output: False

# Greater than or equal to
print(a >= b)  # Output: True

# Less than or equal to
print(a <= b)  # Output: False

'''
3. Logical Operators
Logical operators are used to combine conditional statements.

and: Returns True if both statements are true (e.g., a and b)
or: Returns True if one of the statements is true (e.g., a or b)
not: Reverse the result, returns False if the result is true (e.g., not a)

'''
x = True
y = False

# and
print(x and y)  # Output: False

# or
print(x or y)  # Output: True

# not
print(not x)  # Output: False

'''
4. Assignment Operators
Assignment operators are used to assign values to variables.

=: Assigns a value (e.g., a = 5)
+=: Adds and then assigns (e.g., a += 3 is equivalent to a = a + 3)
-=: Subtracts and then assigns (e.g., a -= 3)
*=: Multiplies and then assigns (e.g., a *= 3)
/=: Divides and then assigns (e.g., a /= 3)
%=: Takes modulus and then assigns (e.g., a %= 3)
**=: Exponentiates and then assigns (e.g., a **= 3)
//=: Performs floor division and then assigns (e.g., a //= 3)
There are more assignment operators related to bitwise operations as well.

'''
a = 5  # Assignment

a += 2  # Add and assign
print(a)  # Output: 7

a -= 2  # Subtract and assign
print(a)  # Output: 5

a *= 2  # Multiply and assign
print(a)  # Output: 10

a /= 2  # Divide and assign
print(a)  # Output: 5.0

a = 16
a %= 7  # Equivalent to a = a % 7
print(a)  # Output: 2

a = 2
a **= 3  # Equivalent to a = a ** 3
print(a)  # Output: 8

a = 7
a //= 2  # Equivalent to a = a // 2
print(a)  # Output: 3


'''
5. Bitwise Operators
Bitwise operators act on bits and perform bit-by-bit operations.

&: Bitwise AND (e.g., a & b)
|: Bitwise OR (e.g., a | b)
^: Bitwise XOR (e.g., a ^ b)
~: Bitwise NOT (e.g., ~a)
<<: Bitwise left shift (e.g., a << 1)
>>: Bitwise right shift (e.g., a >> 1)

'''
a, b = 2, 3  # 2: 10 in binary, 3: 11 in binary

# Bitwise AND
print(a & b)  # Output: 2 (10 in binary) 10 and 11 => 10
'''
10
11
----
10  (which is 2 in decimal)
'''

# Bitwise OR
print(a | b)  # Output: 3 (11 in binary) 10 or 11 => 11 
'''
10
11
----
11  (which is 3 in decimal)

'''
# Bitwise XOR
print(a ^ b)  # Output: 1 (01 in binary)
'''
10
11
----
01  (which is 1 in decimal)

'''
# Bitwise NOT
print(~a)  # Output: -3 (flips all the bits)
# In binary: ~10 becomes 01 (in two's complement, this is -3)\
    
# Bitwise left shift
print(a << 1)  # Output: 4 (shifts left by 1 bit)
# In binary: 10 shifted left by 1 place becomes 100 (which is 4 in decimal)
# Bitwise right shift
print(a >> 1)  # Output: 1 (shifts right by 1 bit)
# In binary: 10 shifted right by 1 place becomes 1 (which is 1 in decimal)
'''
6. Identity Operators
Identity operators compare the memory locations of two objects.
Check if objects are identical (same memory location).
is: Returns True if both variables are the same object (e.g., a is b)
is not: Returns True if both variables are not the same object (e.g., a is not b)

Applicability:
The membership operators in Python, in and not in, 
are broadly applicable to a variety of data types 
beyond just lists. They are used to test whether a 
value or variable is found in a sequence 
(such as a list, tuple, string, or range) 
or a collection (such as a dictionary, set, or frozenset). 

'''
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# is
print(a is b)  # Output: True

# is not
print(a is not c)  # Output: True

'''
7. Membership Operators
Membership operators test if a sequence is presented in an object.

in: Returns True if a sequence with the specified value is present 
in the object (e.g., a in list)
not in: Returns True if a sequence with the specified value is 
not present in the object (e.g., a not in list)

'''
list = [1, 2, 3, 4, 5]

# in
print(3 in list)  # Output: True

# not in
print(6 not in list)  # Output: True


## Strings
greeting = "Hello, World!"
print("World" in greeting)  # Output: True
print("Goodbye" not in greeting)  # Output: True


# Tuples
vowels = ('a', 'e', 'i', 'o', 'u')
print('e' in vowels)  # Output: True
print('y' not in vowels)  # Output: True

# Dictionaries
person = {"name": "Alice", "age": 25}
print("name" in person)  # Output: True
print("address" not in person)  # Output: True

# Set and Frozenset
primes = {2, 3, 5, 7, 11}
print(3 in primes)  # Output: True
print(4 not in primes)  # Output: True

# Range
nums = range(10)
print(5 in nums)  # Output: True
print(15 not in nums)  # Output: True


'''
Walrus Operator:

Walrus Operator (:=)
The Walrus operator, introduced in Python 3.8, is an 
assignment expression operator. It assigns 
values to variables as part of an expression.

Key Features:
Inline Assignments: It allows you to assign 
values to variables within an expression, 
including conditions in loops and comprehensions.
Improves Readability: Can make some parts of the 
code more readable by eliminating the need 
for an assignment statement before the expression.
Efficiency: It can be more efficient in 
some cases as it avoids re-evaluating an expression.
'''

'''
Example1: Getting input
'''
# Without Walrus Operator
input_str = input("Enter something: ")
while input_str != "quit":
    print("You entered:", input_str)
    input_str = input("Enter something: ")

# With Walrus Operator
while (input_str := input("Enter something: ")) != "quit":
    print("You entered:", input_str)
    
'''
Example2: Finding the length of words
'''
# Finding lengths of words using the Walrus operator
words = ["hello", "world", "python", "programming"]
lengths = [(word, len_word) for word in words if (len_word := len(word)) > 6]
print(lengths)