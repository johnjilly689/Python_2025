print("You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:")
print("The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.")
print("In Python, variables are created when you assign a value to it:")
print("Python has no command for declaring a variable.")

#Python Variables

# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# e.g x= 5

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
# e.g x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)

# If you want to specify the data type of a variable, this can be done with casting.

# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# Get the Type
# You can get the data type of a variable with the type() function.
# e.g x = 5
# y = "John"
# print(type(x))
# print(type(y))

# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Python Variables - Assign Multiple Values
# - Python allows you to assign values to multiple variables in one line:
# Note: Make sure the number of variables matches the number of values, or else you will get an error.
#     e.g x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# -And you can assign the same value to multiple variables in one line:
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# -If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

#     -  fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

x=["apple","ball"]
y,z=x
print(y)