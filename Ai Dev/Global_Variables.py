# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

# Create a variable outside of a function, and use it inside the function

x="awesome"
x="wow"
def morning():
    print("python is ",x,"what you say")

morning()

# Local Variable
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x="arun"
def local():
    x="sunita"  #local variable
    print(x)
local()  # local variable print
print(x)  # global variable


# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

y='i am global but will be use under def local as local and inside def i will change my value and return new value of y, i am doing this to show how global keyword works'
def locally():
    global y
    y="i the variable y is now changing myself to a local, using global keyword"
    return y

z=locally()
print(z)