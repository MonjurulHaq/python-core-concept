# Sets are used to store multiple items in a single variable.
# Set items are unchangeable, but we can remove items and add new items.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets cannot have two items with the same value.
# Duplicates Not Allowed
# Once a set is created, we cannot change its items, but we can remove items and add new items.
# The values True and 1 are considered the same value in sets, and are treated as duplicates:

myset = {"apple", "banana", "cherry"}
print (myset)

thisset = {"apple", "banana", "cherry", True, 1, 2, False, 0} # True=1, False = 0 (considerd same value)
print(thisset)
print(len(thisset))

# The set() Constructor
# It is also possible to use the set() constructor to make a set.

# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


#Access Items
# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("banana" not in thisset)


#Adding set items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry", "orange", "mango"}
thisset.remove("cherry")   #If the item to remove does not exist, remove() will raise an error.
print(thisset)
thisset.discard("banana")  #If the item to remove does not exist, discard() will NOT raise an error.
thisset.pop() #Remove a random item by using the pop() method:
print(thisset)


#Join Sets
#There are several ways to join two or more sets in Python.

#The union() and update() methods joins all items from both sets.

#The intersection() method keeps ONLY the duplicates.

#The difference() method keeps the items from the first set that are not in the other set(s).

#The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
