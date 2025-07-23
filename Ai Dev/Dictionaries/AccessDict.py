# // accessing keys
thisdict={
    "brand":"TATA",
    "model":"sub"
}

print(thisdict.keys())

#accessing values
print(thisdict.values())

#accessing items: The items() method will return each item in a dictionary, as tuples in a list.
print(thisdict.items())
print("model" in thisdict)
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")