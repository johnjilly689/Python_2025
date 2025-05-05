#  In Python, the . (dot) operator is used to access attributes and methods of objects.
text = "hello world"
print(text.upper())  # ✅ Calls the `.upper()` method → "HELLO WORLD"
# Here, upper() is a method of the string object, and the . operator is used to call it.

class Dog:
    def __init__(self, name):
        self.name = name  # `name` is an attribute

buddy = Dog("Buddy")
print(buddy.name)  # ✅ Accessing the `name` attribute → "Buddy"