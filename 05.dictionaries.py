thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)

# printing the brand value in this dictionary
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print("Brand: " + thisdict["brand"])

# String, int, boolean, and list data types:
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}

# Duplicate values will overwrite existing values:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
print(thisdict)
print(len(thisdict))
print(type(thisdict))

# Using the dict() method to make a dictionary:
thisdict = dict(name="JOHN", age=23, ID="483587495")
print(thisdict)

# Access the items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
# x = thisdict["model"]
x = thisdict.get("model")
print(x)

# Get a list of the keys:
x = thisdict.keys()
print(x)
thisdict["color"] = "White"
print(thisdict)

# Get a list of the values:
x = thisdict.values()
print(x)

# Check if "model" is present in the dictionary:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Update the "year" of the car by using the update() method:
thisdict.update({"year": 2327})
print(thisdict)

# adding item
thisdict.update({"owner": "John"})
print(thisdict)

# remove item
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
del thisdict  # delete whole dictionary
# print(thisdict)           #shows NameError

# The clear() method empties the dictionary:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)


# Loop Through a Dictionary

# Print all key names in the dictionary, one by one:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in thisdict:
    print(x)

# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

# values() method returns values of a dictionary:
for x in thisdict.values():
    print(x)

# keys() method returns the keys of a dictionary:
for x in thisdict.keys():
    print(x)

# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    print(x, y)


# Copy a Dictionary

# Make a copy of a dictionary with the copy() method:
mydict = thisdict.copy()
print(mydict)

# Make a copy of a dictionary with the dict() function:
mydict = dict(thisdict)


# Nested Dictionaries

# A dictionary that contains three dictionary
myfamily = {
    "child1": {"name": "Emily", "age": 12},
    "child2": {"name": "Joy", "age": 23},
    "child3": {"name": "Mama", "age": 37},
}
print(myfamily["child2"]["name"])

# Loop through the keys and values of all nested dictionaries:
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])