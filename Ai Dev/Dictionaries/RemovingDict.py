#removing or deleting elements or dict itself there are two functions
# pop and del keyword
# pop()
# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.pop("model"))
print(thisdict)

#del keyword: del keyword is used to delete element and variable also

del thisdict["year"]
print(thisdict)

del thisdict
print(thisdict)  # this line will give error because, this dict has been deleted
