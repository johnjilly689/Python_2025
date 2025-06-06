x=range(6)
print(x)

# the range data type is used to generate a sequence of numbers within a specified range. It's commonly used in loops, particularly for loops, where you need to iterate over a sequence of numbers.

# Syntax:
# python
# range(start, stop, step)
# start (optional): The beginning of the sequence (default is 0).
# stop: The endpoint (exclusive, meaning it is not included in the sequence).
# step (optional): The increment between numbers (default is 1).

# Sequence data Types:	list, tuple, range
# Mapping data Type:	dict
# sequence data types can be access by indexing because they are ordered but mapping are unordered so they cannot be access by indexing but by keys

# Python has two Boolean constants:

# python
# True  # Represents logical truth
# False # Represents logical falsehood
# These are case-sensitive, meaning true or false (lowercase) would result in an error.

# Example:
# python
# is_sunny = True
# is_raining = False

# print(is_sunny)  # Output: True
# print(is_raining)  # Output: False
# Boolean in Comparisons
# Boolean values are often generated by comparison operators:

# python
# print(5 > 3)   # Output: True
# print(10 == 5) # Output: False
# print(7 <= 7)  # Output: True
# Boolean in Conditional Statements
# Booleans are commonly used in if statements:

# python
# age = 18

# if age >= 18:
#     print("Eligible to vote!")  # This will execute
# else:
#     print("Not eligible.")
# Boolean and Logical Operators
# Booleans work with logical operators (and, or, not):

# python
# x = True
# y = False

# print(x and y)  # Output: False (Both must be True)
# print(x or y)   # Output: True (At least one must be True)
# print(not x)    # Output: False (Negates the value)
# Boolean Conversion (bool())
# Any value can be converted into a Boolean:

# python
# print(bool(0))         # Output: False
# print(bool(1))         # Output: True
# print(bool(""))        # Output: False (Empty string)
# print(bool("hello"))   # Output: True (Non-empty string)
# print(bool([]))        # Output: False (Empty list)
# print(bool([1, 2]))    # Output: True (Non-empty list)

# will study this two data type later
# Set Types:	set, frozenset
# Binary Types:	bytes, bytearray, memoryview

# NoneType is the type of the special value None, which represents the absence of a value or a null value.

# What is NoneType?
# None is a built-in constant in Python.

# It is used to indicate "no value" or "null".

# NoneType is the type of None, and None is the only value of this type.

# Example: Assigning None
# python
# x = None
# print(x)        # Output: None
# print(type(x))  # Output: <class 'NoneType'>
# Common Uses of None
# Default Return Value for Functions If a function does not return anything explicitly, it automatically returns None:

# python
# def example_function():
#     pass  # No return statement

# result = example_function()
# print(result)  # Output: None
# Indicating Missing or Undefined Values

# python
# def get_data():
#     return None  # Represents a missing value

# data = get_data()
# if data is None:
#     print("No data available.") 